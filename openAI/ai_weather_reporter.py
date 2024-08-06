from openai import OpenAI

client = OpenAI()

def generate_weather_report(data):
    weather_description = data['weather'][0].get('description', 'No description available')
    temperature = data['main'].get('temp', 'No temperature data')
    humidity = data['main'].get('humidity', 'No humidity data')
    feels_like = data['main'].get('feels_like', 'No feels_like data')
    wind_speed = data['wind'].get('speed', 'No wind speed data')
    city_name = data.get('name', 'Unknown city')
    temp_max = data['main'].get('temp_max', 'No max temperature data')
    temp_min = data['main'].get('temp_min', 'No min temperature data')

    # Format the weather report
    weather_report = (
        f"Currently in {city_name}, the weather is described as {weather_description}. "
        f"The temperature is {temperature}° with a feels-like temperature of {feels_like}°. "
        f"The high for today is {temp_max}° and the low is {temp_min}°. "
        f"Humidity is at {humidity}%, and wind speed is {wind_speed} m/s."
    )

    # Generate the AI response
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "system",
            "content": f"You are a weatherman, local to the area provided by the weather information you will receive. Give a weather report based on this information, adding some local flair. Also recommend what type of clothing to wear, or what activities would be nice given the weather. The weather report is: {weather_report}"
        }]
    )

    # Correctly extract the content from the response
    ai_response = response.choices[0].message.content

    return ai_response
