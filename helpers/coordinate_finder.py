from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="coordinateFinder")

def get_coordinates(city: str, state: str) -> tuple[float, float]:
    location = geolocator.geocode(city + ", " + state)

    if location:
        longitude = location.longitude
        latitude = location.latitude
        print("lat", latitude, "long", longitude)
        return (latitude, longitude)

    return (None, None)
