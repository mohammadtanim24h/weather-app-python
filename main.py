import requests as req
import win32com.client as wincom

print("Welcome to Weather App. Created by Tanim")

speak = wincom.Dispatch("SAPI.SpVoice")

# Taking input from the user
city = input("Enter the name of the city: ")
url = f"https://api.weatherapi.com/v1/current.json?key=0039ba140f3348fbb3f44716232504&q={city}"

# Making the request using the user input
r = req.get(url)
weather = r.json()
try:
    speak.Speak(f"The current weather in {city} is {weather['current']['condition']['text']}. The temperature is {weather['current']['temp_c']} degree celsius. It was last updated on {weather['current']['last_updated']}.")

except:
    if weather["error"]["code"] == 1006:
        print(weather["error"]["message"], "Please enter a correct location.")