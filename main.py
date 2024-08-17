from flask import Flask, jsonify
import requests
from helpers.coordinate_finder import get_coordinates
from flask_cors import CORS
from constants import openWeatherKey
from weather_report.ai_weather_reporter import generate_weather_report

app = Flask(__name__)
CORS(app)

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route('/weather/<city>/<state>/<units>', methods=['GET'])
def get_current_weather(city, state, units):
    coordinates = get_coordinates(city, state)
    if coordinates[0] is None or coordinates[1] is None:
        return jsonify({"error": "Invalid coordinates"}), 400

    params = {
        'lat': coordinates[0],
        'lon': coordinates[1],
        'appid': openWeatherKey,
        'units': units,
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=20)
        response.raise_for_status()
    except requests.RequestException as e:
        return jsonify({"Error": str(e)}), 500

    if response.status_code == 200:
        data = response.json()
        weather_report = generate_weather_report(data)
        return jsonify({"weather_report": weather_report})

    return f"Error: {response.status_code}"



if __name__ == '__main__':
    app.run()
