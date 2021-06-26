from json import loads

from opencage.geocoder import OpenCageGeocode
from PySmartMirror.handlers.log import LogHandler
from PySmartMirror.models.location import Location
from PySmartMirror.models.weather import Weather
from requests import get
import feedparser


class NetworkHandler:
    def __init__(self):
        pass

    @staticmethod
    def get_location_from_opencage(api_key, latitude, longitude):
        logger = LogHandler().get_logger()

        location = Location()
        logger.debug(f'Fetching location for latidute {latitude} and longitude {longitude}')
        try:
            geocoder = OpenCageGeocode(api_key)
            results = geocoder.reverse_geocode(latitude, longitude)

            location.city = results[0]['components']['county']
            location.state = results[0]['components']['state']
            location.country_code = results[0]['components']['country_code'].upper()

        except Exception as e:
            logger.error('Failed to get location details')
            logger.exception(e, exc_info=True)

        return location

    @staticmethod
    def get_weather_from_darksky(api_key, latitude, longitude, weather_language, weather_unit):
        logger = LogHandler().get_logger()
        weather = Weather()

        logger.debug(f'Fetching weather updates from darksky.net for latitude {latitude} and longitude {longitude}')
        try:
            weather_request_url = f'https://api.darksky.net/forecast/{api_key}/{latitude},{longitude}?lang={weather_language}&units={weather_unit}'
            weather_response = get(weather_request_url)
            weather_dict = loads(weather_response.text)

            weather.temperature = weather_dict['currently']['temperature']
            weather.current_state = weather_dict['currently']['summary']
            weather.forecast = weather_dict['hourly']['summary']
            weather.icon_text = weather_dict['currently']['icon']

        except Exception as e:
            logger.error('Failed to get weather update')
            logger.exception(e, exc_info=True)

        return weather

    @staticmethod
    def get_feeds_from_google(feed_url, count=10):
        feeds = []
        logger = LogHandler().get_logger()

        logger.debug(f'Fetching maxinum {count} feeds from {feed_url}')

        try:
            google_feeds = feedparser.parse(feed_url)
            for feed in google_feeds.entries[:count]:
                feeds.append(feed.title)

        except Exception as e:
            logger.error('Failed to get location details')
            logger.exception(e, exc_info=True)

        return feeds
