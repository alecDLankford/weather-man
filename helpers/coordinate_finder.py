from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="coordinateFinder")

def get_coordinates(city: str, state: str) -> tuple[float, float]:
    location = geolocator.geocode(city + ", " + state)

    longitude = location.longitude
    latitude = location.latitude

    if location:
        return (latitude, longitude)
    else:
        return (None, None)
