import requests
import json
import pyttsx3
city=input("enter the name of City : \n")
Url=f"https://api.weatherapi.com/v1/current.json?key=06fe370f96594073af6160011241903&q={city}"
engine = pyttsx3.init()
r = requests.get(Url)
print(r.text)
#print(type(r.text))
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
engine.say("the current weather in {city} is {w}degree")
engine.runAndWait()