import json

with open("weather.json", "r") as file:
    data = json.load(file)

city = data["city"]
temperature = data["temperature"]
humidity = data["humidity"]
description = data["description"]

print("----- Current Weather Report------")
print("City:", city)
print("Temperature:", temperature, "°C")
print("Humidity:", humidity, "%")
print("Weather Description:", description)
