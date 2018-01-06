import json
import cloud 
import sys

data = {}
data['mode'] = 'weather'
data['brightness'] = 0.9
data['color'] = cloud.red
data['brightColor'] = cloud.red
data['alarmStart'] = [8, 20];
data['alarmStop'] = [8, 40];


#mode = 'weather'
##A mode switch for the cloud state machine
## 'weather' displays the current weather
## 'alarm' displays the current weather between the set alarm times every morning
## 'lightning' displays a lightning show
## 'rain' displays a rain show
## 'rainbow' displays a rainbow show
## 'color' displays a fixed colour
## 'off' turns the lights off
#
#brightness = 0.9
##[0-1] float which adjusts the relative brightness of the various manual mode functions
#
#color = red
#brightColor = red
##Only applies to the 'color' mode
#
#alarmStart = [8, 20];
#alarmStop = [8, 40];
##The alarm start and stop times as tuples of (hh,mm) in 24 hour time


with open('state.txt', 'w') as outfile:  
    json.dump(data, outfile)
    
sys.exit()
