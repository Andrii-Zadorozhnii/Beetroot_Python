import googlemaps
from django.conf import settings


gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)

def get_route_info(origin, destination):
    try:
        directions = gmaps.directions(origin, destination, mode="driving")
        if directions:
            distance = directions[0]['legs'][0]['distance']['text']
            duration = directions[0]['legs'][0]['duration']['text']
            return {'distance': distance, 'duration': duration}
        else:
            return None
    except googlemaps.exceptions.ApiError as e:
        print(f"Google Maps API error: {e}")
        return None