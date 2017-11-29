import cloud
import datetime
from urllib2 import Request, urlopen, URLError
from displayHelper import *
import json
import time
from neopixel import *

def getWeather():
    #For reference
    #API_KEY 	= 74e3781521968a538eb598a44d263091
    #CITY_ID 	= 6619279
    request = Request('http://api.openweathermap.org/data/2.5/forecast?id=6619279&APPID=caa3c1d9fcc87e07420d987dbdaa99ab')
    
    try:
        response = urlopen(request)
        weatherJSON = response.read()
    
    except URLError, e:
        print 'URL Error while fetching weather. Got an error code:', e
    
    parsedWeather = json.loads(weatherJSON)
     
    weather = parsedWeather['list']
    
    weatherState = 0;
    intensity = 0;
    
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
    temperature = temp - cloud.averages[monthNum]
    
    states = ['clear', 'rain', 'weird', 'storms', 'extreme']
    cloud.weatherState = states[weatherState]
    cloud.intensity = intensity
    cloud.temperature = temperature
         
# -------------------------  Weather Display Functions -----------------------
def showExtreme():
    while(cloud.weatherState == 'extreme'):
        for red in range(0,255,2):
            setColor(Color(red,0,0))
            time.sleep(0.001)
        for red in range (254,0, -2):
            setColor(Color(red,0,0))
            time.sleep(0.001)
    
def showRain():
    print("Displaying rain")
    while(cloud.weatherState == 'rain' and cloud.mode == 'weather'):
        setColor(cloud.blue)
        time.sleep(10)
    
def showWeird():
    while(cloud.weatherState == 'weird' and cloud.mode == 'weather'):
        setColor(cloud.green)
        time.sleep(10)
    
def showStorms():
    while(cloud.weatherState == 'storms' and cloud.mode == 'weather'):
        setColor(cloud.red)
        time.sleep(10)

    
def showTemp():
    print('Displaying temperature difference of: ' + str(cloud.temperature))
    while(cloud.weatherState == 'clear' and cloud.mode == 'weather'):
        if(cloud.temperature > 0):
            tempColor = cloud.temperature * 16
            if(tempColor>127):
                tempColor = 127
            
            tempColor = Color(int(128 + tempColor),0,int(128-tempColor))
        
        else:
            tempColor = (-1*cloud.temperature) * 16
            if(tempColor>127):
                tempColor = 127
            
            tempColor = Color(int(128 - tempColor),0,int(128 + tempColor))
            
        setColor(tempColor)
        time.sleep(10)
    
    
    
    # =================== multithreading example code =======================
class animationThread (threading.Thread):
    def __init__(self, threadID, name,  animation, intensity):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.strip = strip
        self.animation = animation
        self.intensity = intensity
        
    def run(self):
        print("Starting thread " + self.name)
        showAnimation(self.name, self. self.animation, self.intensity)
    
def showAnimation(threadName,  animation, intensity):

    if(animation == "lightning"):
        print("Lightning thread")
    elif(animation == "rain"):
        print("Rain thread")
    elif(animation == "extreme"):
        print("Extreme thread")
        setColor(Color(0,0,0), 0)
        while(1):
            if(stopAnimation):
                print("killing animation")
                threadName.exit()
                
            time.sleep(0.5)
            for red in range(0,255,2):
                setColor(Color(red,0,0), 0)
                time.sleep(0.001)
            for red in range (254,0, -2):
                setColor(Color(red,0,0), 0)
                time.sleep(0.001)
    
    else:
        print("Unknown Animation thread")
