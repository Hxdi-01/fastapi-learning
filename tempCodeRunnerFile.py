response = requests.get ("https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&current_weather=true")
data = response.json()
current = data["current_weather"]
temperature = current["temperature"]
weather = current ["windspeed"]
is_day = current['is_day']

print('Temperature: ', temperature)
print('Windspeed: ', weather)
print('Is day: ', "Yes" if is_day else "No")