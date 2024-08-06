# Weather Report Generator with AI Integration

## Description

This project provides a web service that fetches weather information for a specified location and generates a localized weather report using AI. The service integrates with the OpenWeatherMap API to retrieve weather data and uses OpenAI's GPT-4o-mini model to produce a natural-sounding weather report with local flair.

## Files

### `coordinate_finder.py`

This module contains a function to obtain geographical coordinates (latitude and longitude) for a given city and state.

- **Function:** `get_coordinates(city: str, state: str) -> tuple[float, float]`

  - **Inputs:** City and state names.

  - **Outputs:** Tuple containing latitude and longitude. Returns `(None, None)` if the location cannot be found.

### `ai_weather_reporter.py`

This module generates a weather report using the OpenAI GPT-4o-mini model based on the weather data provided.

- **Function:** `generate_weather_report(data)`

  - **Inputs:** Weather data in JSON format.

  - **Outputs:** AI-generated weather report as a string. The response includes a description of the weather, temperature, and suggestions for clothing or activities.

### `main.py`

This script sets up a Flask web server that interacts with the OpenWeatherMap API to fetch weather data based on coordinates obtained from `coordinate_finder.py` and then uses `ai_weather_reporter.py` to generate a weather report.

- **Route:** `/weather/<city>/<state>/<units>`

  - **Method:** GET

  - **Parameters:**

    - `city`: Name of the city.

    - `state`: Name of the state.

    - `units`: Measurement units (e.g., 'imperial').

  - **Outputs:** JSON object containing the AI-generated weather report.

## Installation

1\. **Clone the Repository:**

```bash

   git clone https://github.com/your-username/weather-report-generator.git

   cd weather-report-generator

```

2\. **Install Dependencies:**

```bash

   pip install -r requirements.txt

```

3\. **Set Up Configuration:**

   - Create a `.env` file in the root directory with your OpenWeatherMap API key:

```bash

     OPENWEATHER_API_KEY=your_api_key_here

```

## Usage

1\. **Start the Flask Server:**

```bash

   python main.py

```

2\. **Access the Weather Report:**

   - Open your browser or use a tool like `curl` or `Postman` to make a GET request:

```

     GET http://127.0.0.1:5000/weather/San%20Francisco/CA/imperial

```

## Examples

- **Example Request:**

```bash

  curl "http://127.0.0.1:5000/weather/New%20York/NY/imperial"

```

- **Example Response:**

```json

  {

    "weather_report": "Currently in New York, the weather is described as clear sky. The temperature is 75°F with a feels-like temperature of 77°F. The high for today is 80°F and the low is 70°F. Humidity is at 60%, and wind speed is 5 m/s. It's a beautiful day to go outside and enjoy some fresh air. Wear light clothing and enjoy a stroll in the park!"

  }

```

## Configuration

- **API Keys:**
  - Ensure you have a valid API key for OpenWeatherMap and set it in the `.env` file.
  - Ensure you have a valid OpenAI key.

## Bug Reporting

If you come across and bugs, please feel free to open an issue.

## Acknowledgements

- **OpenWeatherMap** for weather data.

- **OpenAI** for the GPT-4o-mini model.

- **Geopy** for geocoding functionality.

- **Flask** for web framework.

## Contact Information

For any questions or feedback, please contact Alec Lankford (alec.d.lankford@gmail.com).
