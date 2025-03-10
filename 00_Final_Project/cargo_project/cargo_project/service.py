import googlemaps
from django.conf import settings


def get_route_info(origin, destination):
    gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
    directions = gmaps.directions(origin, destination)

    if directions:
        leg = directions[0]['legs'][0]
        return {
            'distance': leg['distance']['text'],
            'duration': leg['duration']['text'],
        }
    return None