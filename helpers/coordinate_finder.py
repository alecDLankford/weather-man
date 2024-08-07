from typing import Tuple
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="coordinateFinder")

def get_coordinates(city: str, state: str) -> Tuple[float, float]:
    location = geolocator.geocode(city + ", " + state)

    if location:
        longitude = location.longitude
        latitude = location.latitude
        return (latitude, longitude)

    return (None, None)
