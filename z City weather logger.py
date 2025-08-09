# Step 1: Import required modules  
import datetime
from http import client
import json
import asyncio
import httpx
import requests

# Step 2: Create a list of cities with coordinates  
cities = [
    ("Karachi", 24.8607, 67.0011),
    ("Tokyo", 35.6764, 139.6500),
    ("London", 51.5072, -0.1276),
    ("New York", 40.7128, -74.0060)
]

# Step 3: Define a class CityWeather  
class CityWeather:
    def __init__(self, temperature, windspeed, time):
        self.temperature = temperature
        self.windspeed = windspeed
        self.time = time

# Step 4: Define a function to fetch weather data (synchronous)  
def fetch_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)
    try:    
        response.raise_for_status()
        data = response.json()
        current = data ["current_weather"]
        temperature = current ["temperature"]
        windspeed = current ["windspeed"]
        time = current ["time"]
        
        print(f"Temperature: {temperature}")
        print(f"Windspeed: {windspeed}")
        print(f"Time : {time}")
        return {
        "temperature": temperature,
        "windspeed": windspeed,
        "time": time
    }
    except requests.exceptions.RequestException as e:
        print("Error: ", str(e))
        return {"error": "Something went wrong"}

# Step 5: Define a function to fetch weather data asynchronously using httpx  
async def fetch_weather_fast(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            data = response.json()
    
            current = data ["current_weather"]
            temperature = current ["temperature"]
            windspeed = current ["windspeed"]
            time = current ["time"]
            
            print(f"Temperature: {temperature}")
            print(f"Windspeed: {windspeed}")
            print(f"Time : {time}")
            return {
            "temperature": temperature,
            "windspeed": windspeed,
            "time": time
            }
    except httpx.RequestError as e:
        print("Async Error:", str(e))
        return {"error": "Something went wrong"}

# Step 6: Write a function to save data to a JSON file
def save_to_file(data, filename= "weather_data.json"):
    try:
        with open (filename, "w") as f:
            json.dump(data, f, indent = 4)
    except Exception as e:
        print("File Write Error:", str(e))

# Step 7: Write a function to read data from the JSON file  
def read_from_file(filename= "weather_data.json"):
    try:
        with open(filename, "r") as f:
                return json.load(f)
    except Exception as e:
        print("File read error:", str(e))
        return None

# Step 8: Define a main async function to run everything  
async def main():
    weather_data = {}
    for city, lat, lon in cities:
        data = await fetch_weather_fast(lat, lon)
        if "error" not in data:
            weather = CityWeather(**data)
            weather_data[city] = {
                "Temperature" : weather.temperature,
                "Windspeed" : weather.windspeed,
                "Time" : weather.time
            }
    save_to_file(weather_data)

# Step 9: Call asyncio.run(main()) to execute the program  
if __name__ == "__main__":
    asyncio.run(main())