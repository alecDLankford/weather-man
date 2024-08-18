import openai
from gsm import get_secret

def validate_weather_data(data):
    required_fields = {
        'weather_description': data['weather'][0].get('description'),
        'temperature': data['main'].get('temp'),
        'humidity': data['main'].get('humidity'),
        'feels_like': data['main'].get('feels_like'),
        'wind_speed': data['wind'].get('speed'),
        'city_name': data.get('name'),
        'temp_max': data['main'].get('temp_max'),
        'temp_min': data['main'].get('temp_min')
    }

    for _, value in required_fields.items():
        if value is None or (isinstance(value, str) and value.strip() == ''):
            return None

    return required_fields

def generate_weather_report(data):
    openai.api_key = get_secret("open_ai")
    validated_data = validate_weather_data(data)

    if validated_data is None:
        return "Error: One or are weather fields are missing"

    weather_description = validated_data['weather_description']
    temperature = validated_data['temperature']
    humidity = validated_data['humidity']
    feels_like = validated_data['feels_like']
    wind_speed = validated_data['wind_speed']
    city_name = validated_data['city_name']
    temp_max = validated_data['temp_max']
    temp_min = validated_data['temp_min']

    weather_report = (
        f"Currently in {city_name}, the weather is described as {weather_description}. "
        f"The temperature is {temperature}° with a feels-like temperature of {feels_like}°. "
        f"The high for today is {temp_max}° and the low is {temp_min}°. "
        f"Humidity is at {humidity}%, and wind speed is {wind_speed} m/s."
    )

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "system",
            "content": f"You are a weatherman, local to the area provided by the weather information you will receive. Give a weather report based on this information, adding some local flair. Also recommend what type of clothing to wear, or what activities would be nice given the weather. Do not reference the date, and round the degrees to the nearest whole number. Also make sure all measurements are standard imperial degrees and not metric. The weather report is: {weather_report}"
        }]
    )

    ai_response = response.choices[0].message.content

    return ai_response
