# Python METAR Data Reading Program
from lxml import html
import requests

#import Weather_Analysis_GUI as GUI

class Weather_Variables():
    def __init__(self):
        self.names = {
            "station": "Station",
            "valid": "Time",
            "tmpf": "Temperature [F]",
            "tmpc": "Temperature [C]",
            "dwpf": "Dewpoint [F]",
            "relh": "Relative Humidity [%]",
            "drct": "Wind Direction",
            "sknt": "Wind Speed [Knots]",
            "po1i": "Precipitation [Inches]",
            "alti": "Pressure [Inches]",
            "mslp": "Pressure [Mb]",
            "vsby": "Visibility [Miles]",
            "gust": "Wind Gust [Knots]",
            "skyc1": "Sky Level 1 Coverage",
            "skyc2": "Sky Level 2 Coverage",
            "skyc3": "Sky Level 3 Coverage",
            "skyc4": "Sky Level 4 Coverage",
            "skyl1": "Sky Level 1 Altitude [Ft]",
            "skyl2": "Sky Level 2 Altitude [Ft]",
            "skyl3": "Sky Level 3 Altitude [Ft]",
            "skyl4": "Sky Level 4 Altitude [Ft]",
            "wxcodes": "Present Weather Codes",
            "feel": "Apparent Temperature [F]",
            "ice_accretion_1hr": "1 Hour Ice Accretion [Inches]",
            "ice_accretion_3hr": "3 Hour Ice Accretion [Inches]",
            "ice_accretion_6hr": "6 Hour Ice Accretion [Inches]",
            "peak_wind_gust": "Peak Wind Gust [Knots]",
            "peak_wind_drct": "Peak Wind Direction [deg]",
            "peak_wind_time": "Peak Wind Gust Time",
            "metar": "Raw Metar Data"
            }

def webpage(web):
    page = requests.get(web)
    tree = html.fromstring(page.content)
    temperature = tree.xpath('//text()')
    return temperature

def write_file(data):
    file = "weather_data.txt"
    f = open(file,"w+")
    for i in data:
        f.write(i)
    return file

def read_file(file):
    f = open(file,"r")
    read = f.readlines()
    a = []
    
    var = 0
    
    for i in range(len(read)): 
        b = str(read[i]).split(",")
        for v in Weather_Variables().names:
            if v in b:
                var = b.index(v)
                #print(b[var])
            a.append(b)
            
            break        
            
    return a


"""def link():
    b = GUI.Start().answer[0]
    while b is True:
        if GUI.question1().answer[0] == "No":
            a = "weather_data.txt"
            b = False
        elif GUI.question1().answer[0] == "Yes":
            web = GUI.link1()
            web2 = webpage(web)
            a = write_file(web2)
            b = False
    return a"""


    




