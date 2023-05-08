import optuna
import xgboost as xgb
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

from optuna_xgb_param_grid import OptunaXGBParamGrid

# Input
# Given some training data
# Given a model type
# Given some hyperparameters and ranges

# Action
# Split into training and validation sets
# Tune hyperparameters using CV or bootstrapping
# Identify best hyperparameters

# Output
# Hyperparameters from best performing model


class HyperparameterTuner:
    
    def __init__(self, training_data, response):
        self.training_data = training_data
        self.response = response
             
class XGBHyperparameterTuner(HyperparameterTuner, OptunaXGBParamGrid):
    
    def __init__(self, training_data, response) -> None:
        super().__init__(training_data, response)
        
    def objective(self, trial):

        train_x, valid_x, train_y, valid_y = train_test_split(self.training_data, self.response, test_size=self.validation_size)
        dtrain = xgb.DMatrix(train_x, label=train_y)
        dvalid = xgb.DMatrix(valid_x, label=valid_y)

        param = {
            "verbosity": self.verbosity,
            'objective': self.error,
            # maximum depth of the tree, signifies complexity of the tree.
            "max_depth" : trial.suggest_int("max_depth",
                                            self.max_depth_min,
                                            self.max_depth_max,
                                            step=self.max_depth_step),
            # minimum child weight, larger the term more conservative the tree.
            "min_child_weight" : trial.suggest_int("min_child_weight", 
                                                self.min_child_weight_min,
                                                self.min_child_weight_max,
                                                step=self.min_child_weight_step),
            "eta" : trial.suggest_float("eta",
                                        self.eta_min, 
                                        self.eta_max, 
                                        log=True),
            # defines how selective algorithm is.
            "gamma" : trial.suggest_float("gamma", 
                                        self.min_child_weight_max, 
                                        self.min_child_weight_max, 
                                        log=True),
            # L2 regularization weight.
            "lambda": trial.suggest_float("lambda",
                                        self.lambda_min,
                                        self.lambda_max, 
                                        log=True),
            # L1 regularization weight.
            "alpha": trial.suggest_float("alpha", 
                                        self.alpha_min,
                                        self.alpha_max,
                                        log=True),
            # sampling ratio for training data.
            "subsample": trial.suggest_float("subsample", 
                                            self.subsample_min, 
                                            self.subsample_max),
            # sampling according to each tree.
            "colsample_bytree": trial.suggest_float("colsample_bytree",
                                                    self.colsample_bytree_min, 
                                                    self.colsample_bytree_max),
        }        

        bst = xgb.train(param, dtrain)
        preds = bst.predict(dvalid)
        
        rmse = mean_squared_error(preds, valid_y, squared=False)
        
        return rmse

        
    def get_objective_function(self):
        return self.objective
    
    def tune_hyperparameters(self):
    
        self.study = optuna.create_study(direction='minimize')
        self.study.optimize(self.objective, n_trials=self.trials)
        
        print("Number of finished trials: ", len(self.study.trials))
        print("Best trial:")
        trial = self.study.best_trial

        print("  Value: {}".format(trial.value))
        print("  Params: ")
        for key, value in trial.params.items():
            print("    {}: {}".format(key, value))
            
        return self.study
    
    def get_best_params(self):
        return self.study.best_params
            
    