from urllib2 import Request, urlopen, URLError
from lowLevel import *
import json
import time
import datetime
import threading

#Returns a weather state (see below), temperature and an intensity
#The ranges for intensity are:
# storm - 0-2
# rain - 0-4

#Temperature is the mean in Celsius (will be zero for thunderstorms)



def getWeather():
    #Set to get new weather
    updateWeather = 1;
    
    
    #0 - sunny/cloudy
    #1 - rain
    #2 - weird
    #3 - storms
    #4 - extreme 
    
    #For reference
    #API_KEY 	= 74e3781521968a538eb598a44d263091
    #CITY_ID 	= 6619279
    request = Request('http://api.openweathermap.org/data/2.5/forecast?id=6619279&APPID=caa3c1d9fcc87e07420d987dbdaa99ab')
    
    try:
        if(updateWeather):
            response = urlopen(request)
            weatherJSON = response.read()
    
    except URLError, e:
        print 'URL Error while fetching weather. Got an error code:', e
    
    parsedWeather = json.loads(weatherJSON)
     
    weather = parsedWeather['list']
    
    weatherState = 0;
    intensity = 0;
    
    #Calculate temperature relative to monthly average
    averages = [26,26,25,23,20,18,17,18,20,22,24,26]
    temp = 0
    
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
            
        currtemp = currentWeather['main']['temp']-273.15
        if(currtemp > temp):
            temp = currtemp
        
        IDCode = currentWeather['weather'][0]['id']
        IDFirst = IDCode/100
        if(IDCode/10 == 90):
            print("Extreme weather")
            weatherState = 4
            intensity = IDCode%100
            return weatherState
        elif(IDFirst == 2):
            print("Storms")
            if(weatherState<3):
                weatherState = 3
                intensity = IDCode%100
            
        elif(IDFirst == 6 or IDFirst == 7):
            print("Wierd Weather")
            if(weatherState<2):
                weatherState = 2

        elif(IDFirst == 5):
            print("Rain")
            if(weatherState<1):
                weatherState = 1
                intensity = IDCode%100
                

        elif(IDFirst == 8 or IDFirst == 3 or IDFirst == 9 or IDCode == 800 or IDCode == 500):
            print("Clear")
            
        else:
            print("-----Unrecognised Weather!-----")
            
    monthNum = datetime.datetime.now().month
    print('Max Temp Predicted: ' + str(temp))
    temperature = temp - averages[monthNum]
    
    return weatherState, intensity, temperature
         
    #    print('Weather at time '  + ' is:')
    #    print(utc_dt)    
         
# Weather Display Functions -------------
def showExtreme(strip):
    
    setColor(strip, Color(255,0,0),0)
    time.sleep(0.5)
    goDark(strip)
    time.sleep(0.5)
    
def showRain(strip,intensity):
    return
    
def showStorms(strip,intensity):
    return
    
def showTemp(strip,temperature):
    print('Displaying temperature difference of: ' + str(temperature))
    if(temperature > 0):
        tempColor = temperature * 16
        if(tempColor>127):
            tempColor = 127
        
        tempColor = Color(int(128 + tempColor),0,int(128-tempColor))
    
    else:
        tempColor = (-1*temperature) * 16
        if(tempColor>127):
            tempColor = 127
        
        tempColor = Color(int(128 - tempColor),0,int(128 + tempColor))
        
    setColor(strip, tempColor, 0)
    
class animationThread (threading.Thread):
    def __init__(self, threadID, name, strip, animation, intensity):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.strip = strip
        self.animation = animation
        self.intensity = intensity
        
    def run(self):
        print("Starting thread " + self.name)
        showAnimation(self.name, self.strip, self.animation, self.intensity)
    
def showAnimation(threadName, strip, animation, intensity):

    if(animation == "lightning"):
        print("Lightning thread")
    elif(animation == "rain"):
        print("Rain thread")
    elif(animation == "extreme"):
        print("Extreme thread")
        setColor(strip,Color(0,0,0), 0)
        while(1):
            if(stopAnimation):
                print("killing animation")
                threadName.exit()
                
            time.sleep(0.5)
            for red in range(0,255,2):
                setColor(strip,Color(red,0,0), 0)
                time.sleep(0.001)
            for red in range (254,0, -2):
                setColor(strip,Color(red,0,0), 0)
                time.sleep(0.001)
    
    else:
        print("Unknown Animation thread")
