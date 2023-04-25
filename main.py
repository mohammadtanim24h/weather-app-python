import requests as req

print("Welcome to Weather App. Created by Tanim")

# Taking input from the user
city = input("Enter the name of the city: ")
url = f"https://api.weatherapi.com/v1/current.json?key=0039ba140f3348fbb3f44716232504&q={city}"

# Making the request using the user input
r = req.get(url)
weather = r.json()
print(weather["current"])