# Weather Alert

import requests
import time
# from datetime import *
import smtplib, ssl

# for i in range (48):
#     z += "\n"
#     z += time.ctime(data['hourly'][i]['dt'])
#     z += ", "
#     z += str(data['hourly'][i]["weather"][0]["description"]).capitalize()
#     temp = int(data['hourly'][i]["temp"] - 274)
#     z += ", " + str(temp)+" C;\n"


def weather(lat, lon):
    
    weather_parameter = {
        "lat" : lat,
        "lon" : lon,
        "appid" : "bdc08189f66bf0905e17dc8835ad1745",
        "exclude": "minutely,hourly"
    }

    response = requests.get("https://api.openweathermap.org/data/2.5/onecall", weather_parameter)

    response.raise_for_status()

    data = response.json()

    # print(data["current"]["temp"] - 273, data["current"]["weather"][0]["main"])
    # for i in data:
    #     print(i)

    icon = {
        "Clouds" : '\u2601',
        "Thunderstorm" : '\u26c8',
        "Drizzle" : '🌧',
        "Rain" : '\u26C6',
        "Clear" : '\u2600'
    }
    z = f"{data['current']['temp'] - 273:.1f}C {data['current']['weather'][0]['main']}"

    return z

