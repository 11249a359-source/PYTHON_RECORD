AIM:
To fetch weather data from the JSON: Write a python program to fetch current weather
data from the JSON file

ALGORITHM:
1. Start
2. Import the json module
3. Define a function fetch_weather_from_json(file_path)
4. Open the JSON file in read mode
5. Use json.load() to parse the JSON content into a Python dictionary
6. Access the following data from the dictionary:
a) location[&quot;name&quot;] – Name of the city
b) location[&quot;country&quot;] – Name of the country
c) current[&quot;temperature&quot;] – Current temperature
d) current[&quot;humidity&quot;] – Current humidity
e) current[&quot;wind_speed&quot;] – Current wind speed
f) current[&quot;weather_descriptions&quot;][0] – Current weather description
7. Print the weather report in a readable format
8. End the function
9. Call the function with the path to the JSON file

Sample JSON File (weather.json)
{
&quot;location&quot;: {
&quot;name&quot;: &quot;Chennai&quot;,
&quot;country&quot;: &quot;India&quot;
},
&quot;current&quot;: {
&quot;temperature&quot;: 31,
&quot;humidity&quot;: 76,
&quot;wind_speed&quot;: 12,

&quot;weather_descriptions&quot;: [&quot;Partly cloudy&quot;]
}
}

PROGRAM:

import json

def fetch_weather_from_json(file_path):
with open(file_path, &#39;r&#39;) as f:
data = json.load(f)

location = data[&#39;location&#39;][&#39;name&#39;]
country = data[&#39;location&#39;][&#39;country&#39;]
temperature = data[&#39;current&#39;][&#39;temperature&#39;]
humidity = data[&#39;current&#39;][&#39;humidity&#39;]
wind_speed = data[&#39;current&#39;][&#39;wind_speed&#39;]
description = data[&#39;current&#39;][&#39;weather_descriptions&#39;][0]

print(f&quot;Weather Report for {location}, {country}&quot;)
print(f&quot;Condition : {description}&quot;)
print(f&quot;Temperature : {temperature}°C&quot;)
print(f&quot;Humidity : {humidity}%&quot;)
print(f&quot;Wind Speed : {wind_speed} km/h&quot;)
# Example usage
fetch_weather_from_json(&quot;weather.json&quot;)

OUTPUT

Weather Report for Chennai, India
Condition : Partly cloudy
Temperature : 31°C
Humidity : 76%
Wind Speed : 12 km/h
