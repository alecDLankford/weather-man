import unittest
from weather_report.ai_weather_reporter import validate_weather_data

class TestWeatherDataValidation(unittest.TestCase):

    def test_valid_data(self):
        data = {
            'weather': [{'description': 'clear sky'}],
            'main': {
                'temp': '75',
                'humidity': '60',
                'feels_like': '77',
                'temp_max': '80',
                'temp_min': '70'
            },
            'wind': {'speed': '5'},
            'name': 'San Francisco'
        }
        result = validate_weather_data(data)
        self.assertEqual(result, {
            'weather_description': 'clear sky',
            'temperature': '75',
            'humidity': '60',
            'feels_like': '77',
            'wind_speed': '5',
            'city_name': 'San Francisco',
            'temp_max': '80',
            'temp_min': '70'
        })

    def test_missing_field(self):
        data = {
            'weather': [{'description': 'clear sky'}],
            'main': {
                'temp': '75',
                'humidity': '60',
                'feels_like': '77',
                'temp_max': '80'
                # Missing 'temp_min'
            },
            'wind': {'speed': '5'},
            'name': 'San Francisco'
        }
        result = validate_weather_data(data)
        self.assertIsNone(result)

    def test_empty_field(self):
        data = {
            'weather': [{'description': 'clear sky'}],
            'main': {
                'temp': '',  # Empty temperature
                'humidity': '60',
                'feels_like': '77',
                'temp_max': '80',
                'temp_min': '70'
            },
            'wind': {'speed': '5'},
            'name': 'San Francisco'
        }
        result = validate_weather_data(data)
        self.assertIsNone(result)

    def test_all_fields_missing(self):
        data = {
            'weather': [{}],
            'main': {},
            'wind': {},
            'name': ''
        }
        result = validate_weather_data(data)
        self.assertIsNone(result)

    def test_partial_valid_data(self):
        data = {
            'weather': [{'description': 'clear sky'}],
            'main': {
                'temp': '75',
                'humidity': '60',
                'feels_like': None,  # Invalid field
                'temp_max': '80',
                'temp_min': '70'
            },
            'wind': {'speed': '5'},
            'name': 'San Francisco'
        }
        result = validate_weather_data(data)
        self.assertIsNone(result)
