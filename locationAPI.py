from geopy.geocoders import Nominatim
import inquirer


geolocator = Nominatim(user_agent="coordinateFinder")

def get_coordinates() -> tuple[float, float]:
    from constants import locationQuestions

    userInput = inquirer.prompt(locationQuestions)

    city = userInput.get("city")
    state = userInput.get("state")

    location = geolocator.geocode(city + ", " + state)

    longitude = location.longitude
    latitude = location.latitude

    if location:
        return (latitude, longitude)
    else:
        return (None, None)

get_coordinates()