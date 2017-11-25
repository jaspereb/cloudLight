from urllib2 import Request, urlopen, URLError
import json
import datetime
import pytz

#For reference
#API_KEY 	= 74e3781521968a538eb598a44d263091
#CITY_ID 	= 6619279

#Defines

#Set to get new weather
updateWeather = 1;

weatherState = 0;
#0 - sunny/cloudy
#1 - rain
#2 - weird
#3 - storms
#4 - extreme 

local = pytz.timezone ("Australia/Sydney")

#Program
request = Request('http://api.openweathermap.org/data/2.5/forecast?id=6619279&APPID=caa3c1d9fcc87e07420d987dbdaa99ab')

try:
    if(updateWeather):
        response = urlopen(request)
        weatherJSON = response.read()

except URLError, e:
    print 'URL Error while fetching weather. Got an error code:', e

parsedWeather = json.loads(weatherJSON)

#for key, value in parsedWeather.items():
#	print("Key:")
#	print(key)
#	print parsedWeather[key]
 
weather = parsedWeather['list']

for hourly in range(0,len(weather)):
    currentWeather = weather[hourly]

    #Calculate if current weather period is <12 hours away (time is in UTC)
    if (currentWeather['dt'] - time.time()) < 43200:
        print("adding weather")
        print(currentWeather['dt_txt'])
    else:
        print("ignoring weather")
        print(currentWeather['dt_txt'])
        continue
    
    IDCode = currentWeather['weather'][0]['id']
    IDFirst = IDCode/100
    if(IDCode/10 == 90):
        print("Extreme weather")
        weatherState = 4
    elif(IDFirst == 2):
        print("Storms")
        weatherState = 3
    elif(IDFirst == 6 or IDFirst == 7):
        print("Wierd Weather")
        weatherState = 2
    elif(IDFirst == 5):
        print("Rain")
        weatherState = 1
    elif(IDFirst == 8 or IDFirst == 3 or IDFirst == 9 or IDCode == 800 or IDCode == 500)
        print("Clear")
        weatherState = 0
    else:
        print("Unrecognised Weather!")
        weatherState = 5
     
#    print('Weather at time '  + ' is:')
#    print(utc_dt)    
    

#parsedList = json.loads(parsedWeather['list'])