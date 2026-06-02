import json
import logging
import requests
logging.basicConfig(
    filename="weather.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_weather():
    try:
        logging.info("Weather request started")

        response = requests.get(
            "https://api.open-meteo.com/v1/forecast?latitude=13.97&longitude=77.59&current=temperature_2m",
            timeout=5
        )

        data = response.json()

        temperature = data["current"]["temperature_2m"]

        logging.info(f"Temperature fetched: {temperature}")

        return temperature

    except Exception as e:
        logging.error(f"Error occurred: {e}")

        return None
def save_weather(temperature):
    file = open("weather_history.txt", "a")

    file.write(f"{temperature}\n")

    file.close()
    
def save_weather_json(temperature):
    weather_data = {
        "temperature": temperature
    }

    file = open("weather_history.json", "a")

    json.dump(weather_data, file)

    file.write("\n")

    file.close()