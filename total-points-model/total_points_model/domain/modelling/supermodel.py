from total_points_model.domain.contracts.modelling_data_contract import ModellingDataContract

import xgboost as xgb
import joblib

class SuperModel:
    
    def __init__(self, X_train, y_train, X_test, y_test, params):
        """ Model agnostic class that requries training data, test data and parameters.

        Args:
            X_train (Dataframe): Training dataframe including modelling features
            y_train (Array): Training set response
            X_test (Dataframe): Test dataframe including modelling features
            y_test (Array): Test set response
            params (Dict): Model parameters
        """
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test
        self.params = params
    
class SuperXGBRegressor(SuperModel):
    def __init__(self, X_train, y_train, X_test, y_test, params):
        """ XGBoost Regression model that requries training data, test data and parameters.

        Args:
            X_train (Dataframe): Training dataframe including modelling features
            y_train (Array): Training set response
            X_test (Dataframe): Test dataframe including modelling features
            y_test (Array): Test set response
            params (Dict): XGBoost model parameters
        """
        super().__init__(X_train, y_train, X_test, y_test, params)
        
        self.xgb_params = self._get_xgb_hyperparameters()
    
    def _get_xgb_hyperparameters(self):
        """ From given parameters dictionary, gets requried hyperparameters for XGBoost.

        Returns:
            Dict: XGBoost model hyperparameters
        """
        
        return {
            'max_depth': self.params['max_depth'],
            'min_child_weight': self.params['min_child_weight'],
            'eta': self.params['eta'],
            'gamma': self.params['gamma'],
            'lambda': self.params['lambda'],
            'alpha': self.params['alpha'],
            'subsample': self.params['subsample'],
            'colsample_bytree': self.params['colsample_bytree'],
        }
    
    def fit(self):
                
        self.xgb_reg = xgb.XGBRegressor(n_estimators=self.params['num_rounds'],
                                        objective = self.params['objective'],
                                        verbosity = self.params['verbosity'],
                                        early_stopping_rounds = self.params['early_stopping_rounds'],
                                        learning_rate = self.params['eta'],
                                        max_depth = self.params['max_depth'],
                                        min_child_weight = self.params['min_child_weight'],
                                        gamma = self.params['gamma'],
                                        subsample = self.params['subsample'],
                                        colsample_bytree = self.params['colsample_bytree'],
                                        reg_alpha = self.params['alpha'],
                                        reg_lambda = self.params['lambda'],
                                        monotone_constraints = self.params['monotone_constraints']
                                        )
        
        X_train_features = self.X_train.drop(columns = ModellingDataContract.ID_COL)
        X_test_features = self.X_test.drop(columns = ModellingDataContract.ID_COL)
        
        self.xgb_model = self.xgb_reg.fit(X = X_train_features,
                                          y = self.y_train,
                                          eval_set = [(X_train_features, self.y_train), (X_test_features, self.y_test)])
        
    def predict(self, X):
        
        return self.xgb_model.predict(X)
    
    def export_model(self, file_path):
        
        joblib.dump(self.xgb_model, file_path)