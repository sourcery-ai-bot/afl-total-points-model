from dataclasses import dataclass
import numpy as np
@dataclass
class Mappings:
    transformation_mappings = {
        'Round': {
            '01':1,
            '02':2,
            '03':3,
            '04':4,
            '05':5,
            '06':6,
            '07':7,
            '08':8,
            '09':9,
            '10':10,
            '11':11,
            '12':12,
            '13':13,
            '14':14,
            '15':15,
            '16':16,
            '17':17,
            '18':18,
            '19':19,
            '20':20,
            '21':21,
            '22':22,
            '23':23,
            '24':24,
            'F1':25,
            'F2':26,
            'F3':27,
            'F4':28,
            'F5':29
        },
    }
    
    new_feature_mappings = {
        ("Weather_Description", "Kicking_Weather"): {            
            'A coastal few showers.':"Bad Kicking",
            'A few morning showers':"Bad Kicking",
            'A few showers':"Bad Kicking",
            'A few showers Possible storm':"Bad Kicking",
            'A few showers Windy':"Bad Kicking",
            'A few showers clearing.':"Bad Kicking",
            'A few showers clearing. Windy.':"Bad Kicking",
            'A few showers developing':"Bad Kicking",
            'A few showers developing.':"Bad Kicking",
            'A few showers, easing.':"Bad Kicking",
            'A few showers, possible thunderstorm.':"Bad Kicking",
            'A few showers.':"Bad Kicking",
            'A few showers. Chance storm.':"Bad Kicking",
            'A few showers. Windy.':"Bad Kicking",
            'A little drizzle':"Bad Kicking",
            'A little late rain.':"Bad Kicking",
            'A little morning drizzle.':"Bad Kicking",
            'A little rain':"Bad Kicking",
            'A little rain at times.':"Bad Kicking",
            'A little rain clearing. Windy.':"Bad Kicking",
            'A little rain later. Windy.':"Bad Kicking",
            'A little rain tonight.':"Bad Kicking",
            'A little rain.':"Bad Kicking",
            'A little rain. Windy.':"Bad Kicking",
            'A shower or two.':"Bad Kicking",
            'A shower or two. ':"Bad Kicking",
            'Afternoon and evening rain.':"Bad Kicking",
            'Afternoon cool change.':"Bad Kicking",
            'Afternoon shower or two':"Bad Kicking",
            'Afternoon shower or two.':"Bad Kicking",
            'Afternoon showers':"Bad Kicking",
            'Afternoon showers.':"Bad Kicking",
            'Becoming clear.':"Good Kicking",
            'Becoming cloudy':"Good Kicking",
            'Becoming cloudy.':"Good Kicking",
            'Becoming dry.':"Good Kicking",
            'Becoming mostly clear.':"Good Kicking",
            'Becoming mostly sunny':"Good Kicking",
            'Becoming sunny':"Good Kicking",
            'Becoming sunny Windy':"Bad Kicking",
            'Becoming sunny.':"Good Kicking",
            'Becoming windy Mostly sunny':"Bad Kicking",
            'Becoming windy Partly cloudy':"Bad Kicking",
            'Becoming windy Sunny':"Bad Kicking",
            'Becoming windy. Partly cloudy.':"Bad Kicking",
            'Broken Clouds. Cool.':"Good Kicking",
            'Broken Clouds. Mild.':"Good Kicking",
            'Chance morning shower.':"Bad Kicking",
            'Chance of a shower.':"Bad Kicking",
            'Chance of an afternoon shower.':"Bad Kicking",
            'Chance shower.':"Bad Kicking",
            'Clear':"Good Kicking",
            'Clear.':"Good Kicking",
            'Clear. Cool.':"Good Kicking",
            'Clear. Light winds.':"Bad Kicking",
            'Clear. Mild.':"Good Kicking",
            'Cloud clearing':"Good Kicking",
            'Cloud clearing.':"Good Kicking",
            'Cloud increasing':"Good Kicking",
            'Cloud increasing later.':"Good Kicking",
            'Cloud increasing.':"Good Kicking",
            'Cloudy':"Good Kicking",
            'Cloudy morning Sunny afternoon':"Good Kicking",
            'Cloudy periods':"Good Kicking",
            'Cloudy periods.':"Good Kicking",
            'Cloudy periods..':"Good Kicking",
            'Cloudy with isloated showers.':"Bad Kicking",
            'Cloudy with isolated showers.':"Bad Kicking",
            'Cloudy, chance of a shower.':"Bad Kicking",
            'Cloudy, few showers.':"Bad Kicking",
            'Cloudy, possible light shower.':"Bad Kicking",
            'Cloudy, showers.':"Bad Kicking",
            'Cloudy.':"Good Kicking",
            'Cloudy. ':"Good Kicking",
            'Cloudy. Isolated showers.':"Bad Kicking",
            'Cloudy. Local fog.':"Bad Kicking",
            'Cloudy. Mainly fine.':"Good Kicking",
            'Cloudy. Morning fog.':"Bad Kicking",
            'Cloudy. Rain and the chance of thunderstorms.':"Bad Kicking",
            'Cloudy. Scattered showers.':"Bad Kicking",
            'Cool change Partly cloudy':"Good Kicking",
            'Cool, sunny.':"Good Kicking",
            'Drizzle clearing':"Bad Kicking",
            'Drizzle. Broken Clouds. Cool.':"Bad Kicking",
            'Dry and Sunny':"Good Kicking",
            'Dry day':"Good Kicking",
            'Dry day.':"Good Kicking",
            'Dry day. Showers overnight.':"Bad Kicking",
            'Dry. Cloud increasing. Windy.':"Bad Kicking",
            'Early fog Evening showers':"Bad Kicking",
            'Early fog Possible shower':"Bad Kicking",
            'Early fog and frost. Sunny.':"Bad Kicking",
            'Early fog or drizzle clearing.':"Bad Kicking",
            'Early fog then mostly sunny':"Bad Kicking",
            'Early fog then sunny':"Bad Kicking",
            'Early fog. Shower or two.':"Bad Kicking",
            'Early frost Mostly sunny':"Bad Kicking",
            'Early frost. Partly cloudy':"Bad Kicking",
            'Early shower Dry afternoon':"Bad Kicking",
            'Early shower or two':"Bad Kicking",
            'Evening rain.':"Bad Kicking",
            'Evening shower.':"Bad Kicking",
            'Evening showers':"Bad Kicking",
            'Few showers':"Bad Kicking",
            'Few showers Possible storm':"Bad Kicking",
            'Few showers Windy':"Bad Kicking",
            'Few showers clearing later':"Bad Kicking",
            'Few showers clearing later.':"Bad Kicking",
            'Few showers easing':"Bad Kicking",
            'Few showers easing.':"Bad Kicking",
            'Few showers, easing later.':"Bad Kicking",
            'Few showers, possible thunderstorm':"Bad Kicking",
            'Few showers.':"Bad Kicking",
            'Few showers. Windy.':"Bad Kicking",
            'Fine':"Good Kicking",
            'Fine and clear.':"Good Kicking",
            'Fine and partly cloudy.':"Good Kicking",
            'Fine and sunny.':"Good Kicking",
            'Fine,':"Good Kicking",
            'Fine, clear.':"Good Kicking",
            'Fine, cloudy. Windy evening.':"Bad Kicking",
            'Fine, mostly clear.':"Good Kicking",
            'Fine, mostly sunny.':"Good Kicking",
            'Fine, partly cloudy':"Good Kicking",
            'Fine, partly cloudy.':"Good Kicking",
            'Fine, sunny.':"Good Kicking",
            'Fine.':"Good Kicking",
            'Fine. Clear.':"Good Kicking",
            'Fine. Cloudy.':"Good Kicking",
            'Fine. Mostly clear.':"Good Kicking",
            'Fine. Mostly sunny.':"Good Kicking",
            'Fine. Partly cloudy.':"Good Kicking",
            'Fine. Some high cloud.':"Good Kicking",
            'Fine. Sunny.':"Good Kicking",
            'Fog clearing. Late showers. developing.':"Bad Kicking",
            'Fog or drizzle patches clearing.':"Bad Kicking",
            'Further showers Possible storm':"Bad Kicking",
            'Haze':"Bad Kicking",
            'Hazy':"Bad Kicking",
            'Heavy rain':"Bad Kicking",
            'High cloud.':"Good Kicking",
            'Humid Possible shower':"Bad Kicking",
            'Isolated showers.':"Bad Kicking",
            'Late rain':"Bad Kicking",
            'Late rain.':"Bad Kicking",
            'Late rain. Windy.':"Bad Kicking",
            'Late rain/possible storm.':"Bad Kicking",
            'Late shower or storm':"Bad Kicking",
            'Late shower or two':"Bad Kicking",
            'Late shower or two.':"Bad Kicking",
            'Late showers':"Bad Kicking",
            'Late showers Possible storm':"Bad Kicking",
            'Light Rain. Broken Clouds. Cool.':"Bad Kicking",
            'Light Rain. Broken Clouds. Warm.':"Bad Kicking",
            'Light Rain. Partly Cloudy. Mild.':"Bad Kicking",
            'Light Rain. Partly Sunny. Cool.':"Bad Kicking",
            'Light Rain. Partly Sunny. Mild.':"Bad Kicking",
            'Light morning rain.':"Bad Kicking",
            'Light morning shower or two.':"Bad Kicking",
            'Light rain at times':"Bad Kicking",
            'Light shower clearing early.':"Bad Kicking",
            'Light shower or two':"Bad Kicking",
            'Light shower or two.':"Bad Kicking",
            'Light shower two.':"Bad Kicking",
            'Light shower.':"Bad Kicking",
            'Light showers clearing':"Bad Kicking",
            'Light showers or drizzle':"Bad Kicking",
            'Little rain later.':"Bad Kicking",
            'Local fog then sunny':"Bad Kicking",
            'Local morning drizzle clearing.':"Bad Kicking",
            'Mainly clear.':"Good Kicking",
            'Mainly cloudy, a few showers.':"Bad Kicking",
            'Mainly dry.':"Good Kicking",
            'Mainly fine':"Good Kicking",
            'Mainly fine and cloudy.':"Good Kicking",
            'Mainly fine.':"Good Kicking",
            'Mainly sunny.':"Good Kicking",
            'Mild':"Good Kicking",
            'Morning fog':"Bad Kicking",
            'Morning fog and frost':"Bad Kicking",
            'Morning fog and frost.':"Bad Kicking",
            'Morning fog clearing':"Bad Kicking",
            'Morning fog or drizzle.':"Bad Kicking",
            'Morning fog then mostly sunny':"Bad Kicking",
            'Morning fog then partly cloudy':"Bad Kicking",
            'Morning fog then sunny':"Bad Kicking",
            'Morning fog then sunny.':"Bad Kicking",
            'Morning fog, then sunny':"Bad Kicking",
            'Morning fog.':"Bad Kicking",
            'Morning fog. Shower or two.':"Bad Kicking",
            'Morning fog. Sunny afternoon.':"Bad Kicking",
            'Morning frost':"Bad Kicking",
            'Morning frost Cloudy':"Bad Kicking",
            'Morning frost Partly cloudy':"Bad Kicking",
            'Morning frost and fog':"Bad Kicking",
            'Morning frost. Mostly sunny.':"Bad Kicking",
            'Morning rain then showers':"Bad Kicking",
            'Morning rain then showers.':"Bad Kicking",
            'Morning rain, clearing.':"Bad Kicking",
            'Morning shower or two':"Bad Kicking",
            'Morning shower or two then sunny':"Bad Kicking",
            'Morning shower or two.':"Bad Kicking",
            'Morning showers':"Bad Kicking",
            'Morning smoke haze Shower or two':"Bad Kicking",
            'Morning storms. Showers.':"Bad Kicking",
            'Mostly Clear':"Good Kicking",
            'Mostly Clear.':"Good Kicking",
            'Mostly Cloudy. Mild.':"Good Kicking",
            'Mostly Fine':"Good Kicking",
            'Mostly Fine,possible shower or two.':"Bad Kicking",
            'Mostly Sunny':"Good Kicking",
            'Mostly Sunny. Cool.':"Good Kicking",
            'Mostly Sunny. Cool. Breezy.':"Good Kicking",
            'Mostly clear':"Good Kicking",
            'Mostly clear.':"Good Kicking",
            'Mostly clear. Isolated showers.':"Bad Kicking",
            'Mostly cloudy':"Good Kicking",
            'Mostly cloudy.':"Good Kicking",
            'Mostly cloudy. Isolated showers.':"Bad Kicking",
            'Mostly dry':"Good Kicking",
            'Mostly dry Cloudy':"Good Kicking",
            'Mostly dry day Windy':"Bad Kicking",
            'Mostly dry day.':"Good Kicking",
            'Mostly dry.':"Good Kicking",
            'Mostly fine':"Good Kicking",
            'Mostly fine though partly cloudy. ':"Good Kicking",
            'Mostly fine, light shower or two.':"Bad Kicking",
            'Mostly fine, possible shower':"Bad Kicking",
            'Mostly fine, possible shower.':"Bad Kicking",
            'Mostly fine.':"Good Kicking",
            'Mostly fine. Cloudy periods.':"Good Kicking",
            'Mostly sun':"Good Kicking",
            'Mostly sunny':"Good Kicking",
            'Mostly sunny Wind easing':"Bad Kicking",
            'Mostly sunny Windy':"Bad Kicking",
            'Mostly sunny morning.':"Good Kicking",
            'Mostly sunny with light winds':"Bad Kicking",
            'Mostly sunny.':"Good Kicking",
            'Night. Clear':"Good Kicking",
            'Night. Clear.':"Good Kicking",
            'Night. Fine.':"Good Kicking",
            'Night. Mostly Clear':"Good Kicking",
            'Night. Mostly Clear.':"Good Kicking",
            'Overcast. Cool':"Good Kicking",
            'Partly Cloudy':"Good Kicking",
            'Partly Cloudy.':"Good Kicking",
            'Partly Cloudy. Cool.':"Good Kicking",
            'Partly Sunny. Cool.':"Good Kicking",
            'Partly Sunny. Mild.':"Good Kicking",
            'Partly cloudy':"Good Kicking",
            'Partly cloudy Becoming windy':"Bad Kicking",
            'Partly cloudy Possible late shower':"Bad Kicking",
            'Partly cloudy Windy':"Bad Kicking",
            'Partly cloudy with scattered showers.':"Bad Kicking",
            'Partly cloudy,':"Good Kicking",
            'Partly cloudy, isolated showers.':"Bad Kicking",
            'Partly cloudy.':"Good Kicking",
            'Partly cloudy. ':"Good Kicking",
            'Partly cloudy. Evening rain.':"Bad Kicking",
            'Partly cloudy. Isolated showers.':"Bad Kicking",
            'Partly cloudy. Light winds.':"Bad Kicking",
            'Partly cloudy. Scattered showers.':"Bad Kicking",
            'Partly cloudy. Showers increasing.':"Bad Kicking",
            'Partly cloudy. Windy.':"Bad Kicking",
            'Party Cloudy.':"Good Kicking",
            'Passing Clouds':"Good Kicking",
            'Passing Clouds. Cool.':"Good Kicking",
            'Passing Clouds. Cool. Humid.':"Good Kicking",
            'Passing Clouds. Mild.':"Good Kicking",
            'Passing Clouds. Warm.':"Good Kicking",
            'Patchy rain developing':"Bad Kicking",
            'Patchy rain.':"Bad Kicking",
            'Possible afternoon shower':"Bad Kicking",
            'Possible early shower':"Bad Kicking",
            'Possible late shower':"Bad Kicking",
            'Possible late shower Windy':"Bad Kicking",
            'Possible late shower.':"Bad Kicking",
            'Possible light morning shower.':"Bad Kicking",
            'Possible light shower':"Bad Kicking",
            'Possible light shower.':"Bad Kicking",
            'Possible morning drizzle':"Bad Kicking",
            'Possible morning fog':"Bad Kicking",
            'Possible morning fog, then sunny':"Bad Kicking",
            'Possible morning fog.':"Bad Kicking",
            'Possible morning frost.':"Bad Kicking",
            'Possible morning shower':"Bad Kicking",
            'Possible morning shower.':"Bad Kicking",
            'Possible shower':"Bad Kicking",
            'Possible shower Windy':"Bad Kicking",
            'Possible shower developing':"Bad Kicking",
            'Possible shower developing.':"Bad Kicking",
            'Possible shower or storm, clearing':"Bad Kicking",
            'Possible shower or two.':"Bad Kicking",
            'Possible shower, late rain':"Bad Kicking",
            'Possible shower.':"Bad Kicking",
            'Possible shower. Windy.':"Bad Kicking",
            'Rain':"Bad Kicking",
            'Rain Windy Possible heavy falls':"Bad Kicking",
            'Rain at times':"Bad Kicking",
            'Rain at times Possible storm':"Bad Kicking",
            'Rain at times Windy':"Bad Kicking",
            'Rain at times, easing.':"Bad Kicking",
            'Rain at times.':"Bad Kicking",
            'Rain at times. Windy.':"Bad Kicking",
            'Rain clearing':"Bad Kicking",
            'Rain clearing later.':"Bad Kicking",
            'Rain clearing. Wind easing.':"Bad Kicking",
            'Rain developing':"Bad Kicking",
            'Rain developing Becoming windy':"Bad Kicking",
            'Rain developing later':"Bad Kicking",
            'Rain developing.':"Bad Kicking",
            'Rain developing. Very windy.':"Bad Kicking",
            'Rain developing. Windy.':"Bad Kicking",
            'Rain easing':"Bad Kicking",
            'Rain easing Windy':"Bad Kicking",
            'Rain easing.':"Bad Kicking",
            'Rain easing. Windy.':"Bad Kicking",
            'Rain increasing Becoming windy':"Bad Kicking",
            'Rain periods':"Bad Kicking",
            'Rain periods Possible storm Windy':"Bad Kicking",
            'Rain periods Very windy':"Bad Kicking",
            'Rain periods.':"Bad Kicking",
            'Rain this evening.':"Bad Kicking",
            'Rain, easing later.':"Bad Kicking",
            'Rain, easing to showers':"Bad Kicking",
            'Rain, heavy at times.':"Bad Kicking",
            'Rain.':"Bad Kicking",
            'Scattered Clouds. Cool.':"Good Kicking",
            'Scattered Clouds. Mild.':"Good Kicking",
            'Scattered Clouds. Warm.':"Good Kicking",
            'Scattered Showers. Broken Clouds. Cool.':"Bad Kicking",
            'Scattered Showers. Broken Clouds. Mild.':"Bad Kicking",
            'Scattered Showers. Partly Cloudy. Mild.':"Bad Kicking",
            'Scattered Showers. Partly Sunny. Mild.':"Bad Kicking",
            'Scattered Showers. Passing Clouds. Cool.':"Bad Kicking",
            'Scattered showers':"Bad Kicking",
            'Scattered showers, sunny afternoon.':"Bad Kicking",
            'Shower or two':"Bad Kicking",
            'Shower or two Possible storm':"Bad Kicking",
            'Shower or two Wind easing':"Bad Kicking",
            'Shower or two Windy':"Bad Kicking",
            'Shower or two clearing':"Bad Kicking",
            'Shower or two clearing.':"Bad Kicking",
            'Shower or two developing':"Bad Kicking",
            'Shower or two developing Windy':"Bad Kicking",
            'Shower or two developing.':"Bad Kicking",
            'Shower or two increasing later.':"Bad Kicking",
            'Shower or two increasing to rain.':"Bad Kicking",
            'Shower or two increasing.':"Bad Kicking",
            'Shower or two later Windy':"Bad Kicking",
            'Shower or two overnight.':"Bad Kicking",
            'Shower or two, clearing':"Bad Kicking",
            'Shower or two, clearing.':"Bad Kicking",
            'Shower or two, increasing later.':"Bad Kicking",
            'Shower or two, possible thunderstorm.':"Bad Kicking",
            'Shower or two.':"Bad Kicking",
            'Shower or two. Becoming windy.':"Bad Kicking",
            'Shower or two. Wind easing.':"Bad Kicking",
            'Showers':"Bad Kicking",
            'Showers Becoming windy':"Bad Kicking",
            'Showers Local hail and thunder':"Bad Kicking",
            'Showers Possible storm':"Bad Kicking",
            'Showers Squally winds':"Bad Kicking",
            'Showers Wind easing':"Bad Kicking",
            'Showers Windy':"Bad Kicking",
            'Showers and chance of a storm.':"Bad Kicking",
            'Showers and drizzle easing.':"Bad Kicking",
            'Showers and drizzle.':"Bad Kicking",
            'Showers and storm clearing later.':"Bad Kicking",
            'Showers at times':"Bad Kicking",
            'Showers clearing':"Bad Kicking",
            'Showers clearing later':"Bad Kicking",
            'Showers clearing.':"Bad Kicking",
            'Showers developing':"Bad Kicking",
            'Showers developing Becoming windy':"Bad Kicking",
            'Showers developing Possible storm':"Bad Kicking",
            'Showers developing Windy':"Bad Kicking",
            'Showers developing, storm risk.':"Bad Kicking",
            'Showers developing.':"Bad Kicking",
            'Showers easing':"Bad Kicking",
            'Showers easing Very windy':"Bad Kicking",
            'Showers easing later':"Bad Kicking",
            'Showers easing.':"Bad Kicking",
            'Showers increasing':"Bad Kicking",
            'Showers increasing later.':"Bad Kicking",
            'Showers increasing.':"Bad Kicking",
            'Showers increasing. Becoming windy.':"Bad Kicking",
            'Showers mainly morning.':"Bad Kicking",
            'Showers mainly tonight.':"Bad Kicking",
            'Showers, clearing later':"Bad Kicking",
            'Showers, easing this afternoon.':"Bad Kicking",
            'Showers, hail and thunder. Windy.':"Bad Kicking",
            'Showers, possibly heavy':"Bad Kicking",
            'Showers, storm risk.':"Bad Kicking",
            'Showers.':"Bad Kicking",
            'Showers. Possible storm.':"Bad Kicking",
            'Showers. Windy.':"Bad Kicking",
            'Showers/winds increasing.':"Bad Kicking",
            'Sunny':"Good Kicking",
            'Sunny Mild.':"Good Kicking",
            'Sunny day Late shower or two':"Bad Kicking",
            'Sunny day. Late shower or two.':"Bad Kicking",
            'Sunny morning Shower or two':"Bad Kicking",
            'Sunny periods':"Good Kicking",
            'Sunny periods developing.':"Good Kicking",
            'Sunny with light winds.':"Bad Kicking",
            'Sunny, Light winds':"Bad Kicking",
            'Sunny, Mild.':"Good Kicking",
            'Sunny, windy.':"Bad Kicking",
            'Sunny.':"Good Kicking",
            'Sunny. Cold. ':"Good Kicking",
            'Sunny. Cool.':"Good Kicking",
            'Sunny. Mild.':"Good Kicking",
            'Sunny. Warm.':"Good Kicking",
            'Windy':"Bad Kicking",
            'Windy Becoming cloudy':"Bad Kicking",
            'Windy Clear':"Bad Kicking",
            'Windy Late showers':"Bad Kicking",
            'Windy Mostly clear':"Bad Kicking",
            'Windy Mostly sunny':"Bad Kicking",
            'Windy Partly cloudy':"Bad Kicking",
            'Windy Rain at night':"Bad Kicking",
            'Windy Shower or two':"Bad Kicking",
            'Windy Sunny':"Bad Kicking",
            'Windy with rain':"Bad Kicking",
            'Windy.':"Bad Kicking",
            'Windy. A little late rain.':"Bad Kicking",
            'Windy. Cloudy.':"Bad Kicking",
            'Windy. Mainly sunny.':"Bad Kicking",
            'Windy. Mostly clear.':"Bad Kicking",
            'Windy. Mostly sunny.':"Bad Kicking",
            'Windy. Partly cloudy.':"Bad Kicking",
            'Windy. Showers.':"Bad Kicking",
            np.nan:"Bad Kicking"
            },
        ("City", "State"): {
            'Adelaide':"South Australia",
            'Alice Springs':'Northern Territory',
            'Ballarat':"Victoria",
            'Brisbane':"Queensland",
            'Cairns':"Queensland",
            'Canberra':"New South Wales",
            'Darwin':"Northern Territory",
            'Geelong':"Victoria",
            'Gold Coast':"Queensland",
            'Hobart':"Tasmania",
            'Launceston':"Tasmania",
            'Melbourne':"Victoria",
            'Perth':"Western Australia",
            'Shanghai':"International",
            'Sydney':"New South Wales",
            'Townsville':"Queensland"
            },
        ("City", "Victoria"):{
            'Adelaide':"Not Victoria",
            'Alice Springs':'Not Victoria',
            'Ballarat':"Victoria",
            'Brisbane':"Not Victoria",
            'Cairns':"Not Victoria",
            'Canberra':"Not Victoria",
            'Darwin':"Not Victoria",
            'Geelong':"Victoria",
            'Gold Coast':"Not Victoria",
            'Hobart':"Not Victoria",
            'Launceston':"Not Victoria",
            'Melbourne':"Victoria",
            'Perth':"Not Victoria",
            'Shanghai':"Victoria",
            'Sydney':"Not Victoria",
            'Townsville':"Not Victoria"
            },
        ("Venue", "Roof"):{
            'Adelaide Oval':"No Roof",
            'Bellerive Oval':"No Roof",
            'Carrara':"No Roof",
            'Cazalys Stadium':"No Roof",
            'Docklands':"Roof",
            'Eureka Stadium':"No Roof",
            'Gabba':"No Roof",
            'Jiangwan Stadium':"No Roof",
            'Kardinia Park':"No Roof",
            'M.C.G.':"No Roof",
            'Manuka Oval':"No Roof",
            'Marrara Oval':"No Roof",
            'Perth Stadium':"No Roof",
            'Riverway Stadium':"No Roof",
            'S.C.G.':"No Roof",
            'Stadium Australia':"No Roof",
            'Sydney Showground':"No Roof",
            'Traeger Park':"No Roof",
            'York Park':"No Roof"
        }
    }
    meta_mappings = {
        ("Team", "State"): {
            'Adelaide':"South Australia",
            'Brisbane Lions':"Queensland",
            'Carlton':"Victoria",
            'Collingwood':"Victoria",
            'Essendon':"Victoria",
            'Fremantle':"Western Australia",
            'Geelong':"Victoria",
            'Gold Coast':"Queensland",
            'Greater Western Sydney':"New South Wales",
            'Hawthorn':"Victoria",
            'Melbourne':"Victoria",
            'North Melbourne':"Victoria",
            'Port Adelaide':"South Australia",
            'Richmond':"Victoria",
            'St Kilda':"Victoria",
            'Sydney':"New South Wales",
            'West Coast':"Western Australia",
            'Western Bulldogs':"Victoria"}
    }
    