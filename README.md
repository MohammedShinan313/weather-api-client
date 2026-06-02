# 🌦️ Weather API Client (Python)

A lightweight Python CLI application that fetches real-time weather data using the Open-Meteo API.

Built to understand core backend fundamentals including API integration, JSON parsing, error handling, and project structuring in Python.

---

## 🚀 Features

- Real-time weather data fetching
- Temperature, humidity, and wind speed display
- API integration using Open-Meteo
- JSON response parsing
- Basic logging for execution tracking
- Error handling using try/except
- Local file storage for weather data

---

## 🧠 Concepts Used

- REST API integration (`requests`)
- JSON parsing
- Python logging module
- Exception handling (try/except)
- File handling (JSON/text)
- Virtual environments (venv)
- Dependency management (pip)
- Git & GitHub workflow

---

## 🛠️ Tech Stack

- Python 3
- Requests library
- Open-Meteo API
- Git & GitHub

---

## 📁 Project Structure
weather-api-client/
│
├── main.py
├── weather.py
├── requirements.txt
├── weather.log
├── weather_history.json
└── README.md

---

## ⚙️ Setup & Run

```bash
git clone https://github.com/your-username/weather-api-client.git
cd weather-api-client
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
python main.py
