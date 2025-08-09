import requests

response = requests.get ("https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&current_weather=true")
data = response.json()
current = data["current_weather"]
temperature = current["temperature"]
weather = current ["windspeed"]
is_day = current['is_day']

print('Temperature: ', temperature)
print('Windspeed: ', weather)
print('Is day: ', "Yes" if is_day else "No")
lat = 35
lon = 139
url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
response = requests.get(url)
try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    current = data['current_weather']
    print('Temperature: ', current['temperature'])
except requests.exceptions.RequestException as e:
    print("Request Failed: ", e) 

def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    try: 
        response = requests.get(url)
        response.raise_for_status
        current = response.json['current_weather']
        return {
           'temperature': current['temperature'],
            'windspeed': current['windspeed'],
            'is_day': current['is_day'] }
    except requests.exceptions.RequestException as e:
        print("Error: ", str(e))
    
lat = int(input('Enter latitude: '))
lon = int(input('Enter longitude: '))

