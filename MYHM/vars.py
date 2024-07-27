global city, weatherapi
#User Variables 
city = 34221 #This can be either a ZIP code or city, test with weatherapi to get this figured out.
weatherapi = '46dc98daa8574d81ac930006242507' #key from weatherapi.com

#Dynamic Variables
#DO NOT EDIT BEYOND THIS LINE
def customCurrentTime():
    return datetime.now().strftime('%I:%M %p')

def currentWeatherIcon():
    weatherurl = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={weatherapi}&q={city}&days=1").json()
    iconresponse = weatherurl['current']['condition']['icon']
    return f"https:{iconresponse}"

def currentWeatherTemp():
    weatherurl = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={weatherapi}&q={city}&days=1").json()
    tempresponse = round(weatherurl['current']['feelslike_f'])
    return f"{tempresponse}°F"

def currentWeatherHumidity():
    weatherurl = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={weatherapi}&q={city}&days=1").json()
    humitidyresponse = weatherurl['current']['humidity']
    return f"{humitidyresponse}%"


addDRPCValue("custom_time", customCurrentTime)
addDRPCValue("weathericon", currentWeatherIcon)
addDRPCValue("temperature", currentWeatherTemp)
addDRPCValue("humidity", currentWeatherHumidity)

#MYHM 398620861634183188