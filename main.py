from helpers.coordinate_finder import get_coordinates
from flask import Flask, jsonify
from constants import openWeatherKey
from openAI.ai_weather_reporter import generate_weather_report
import requests;



app = Flask(__name__)

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
        'units': 'imperial',
    }

    full_url = requests.Request('GET', BASE_URL, params=params).prepare().url
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather_report = generate_weather_report(data)
        # Extract the OpenAI response
        return jsonify({"weather_report": weather_report})
    else:
        return f"Error: {response.status_code}"



if __name__ == '__main__':
    app.run()
