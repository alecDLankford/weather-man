from locationAPI import get_coordinates
from flask import Flask, jsonify
from constants import openWeatherKey
import requests;



app = Flask(__name__)

base_url = "https://api.openweathermap.org/data/2.5/weather"

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
    
    full_url = requests.Request('GET', base_url, params=params).prepare().url
    print(f"Requesting URL: {full_url}")
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(data)
        print("success")
        return data
    else:
        print("error")
        return f"Error: {response.status_code}"



if __name__ == '__main__':
    app.run()