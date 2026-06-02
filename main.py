from weather import get_weather, save_weather_json
temp = get_weather()

print(f"Current Temperature: {temp}°C")

save_weather_json(temp)