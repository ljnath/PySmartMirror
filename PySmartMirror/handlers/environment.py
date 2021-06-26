import os

from PySmartMirror.common.singleton import Singleton


class Environment(metaclass=Singleton):
    """
    Singleton environment class which stores all user configuration as well as graphics file name
    """
    def __init__(self):
        self.__assets_directory = os.path.dirname(os.path.realpath(__file__))
        self.__images = {
            'clear-day': "Sun.png",                     # clear sky day
            'wind': "Wind.png",                         # wind
            'cloudy': "Cloud.png",                      # cloudy day
            'partly-cloudy-day': "PartlySunny.png",     # partly cloudy day
            'rain': "Rain.png",                         # rain day
            'snow': "Snow.png",                         # snow day
            'snow-thin': "Snow.png",                    # sleet day
            'fog': "Haze.png",                          # fog day
            'clear-night': "Moon.png",                  # clear sky night
            'partly-cloudy-night': "PartlyMoon.png",    # scattered clouds night
            'thunderstorm': "Storm.png",                # thunderstorm
            'tornado': "Tornado.png",                   # tornado
            'hail': "Hail.png",                         # hail
            'twitter': "twitter.png",
            'feeds': "feed.png"
        }

    def populate(self, configs):
        """
        Method to populate the environmental variabled with user configuration
        :param config : config as dict. Configuration values in the form of a dictionary
        """
        self.__font = configs['font_family']
        self.__locale = configs['locale']
        self.__weather_language = self.__locale
        self.__weather_unit = configs['unit']

        self.__feed_url = configs['feed_url']

        self.__24H_format = configs['24H_format']

        self.__xl_font_size = configs['font_size']['xl']
        self.__l_font_size = configs['font_size']['l']
        self.__m_font_size = configs['font_size']['m']
        self.__s_font_size = configs['font_size']['s']

        self.__background_color = configs['color']['background']
        self.__foreground_color = configs['color']['foreground']
        self.__font = configs['font_family']
        self.__locale = configs['locale']

        self.__latitude = configs['location']['latitude']
        self.__longitude = configs['location']['longitude']

        self.__location_api_token = configs['api_key']['opencagedata.com']
        self.__weather_api_token = configs['api_key']['darksky.net']

    def get_image_path(self, image_type):
        """
        Method to return the aboslute path of images based on passed image_type
        If image type is missing, then None is retuned
        :param image_type : image_type as str. Type of image to look for
        :return image_path : image_path as str.
        """
        image_path = None
        if image_type in self.__images.keys():
            image_path = f'{self.__assets_directory}/../assets/{self.__images[image_type]}'

        if not os.path.exists(image_path) or not os.path.isfile(image_path):
            image_path = None

        return image_path

    @property
    def font_size_xl(self):
        return self.__xl_font_size

    @property
    def font_size_l(self):
        return self.__l_font_size

    @property
    def font_size_m(self):
        return self.__m_font_size

    @property
    def font_size_s(self):
        return self.__s_font_size

    @property
    def background_color(self):
        return self.__background_color

    @property
    def foreground_color(self):
        return self.__foreground_color

    @property
    def font(self):
        return self.__font

    @property
    def locale(self):
        return self.__locale

    @property
    def latitude(self):
        return self.__latitude

    @property
    def longitude(self):
        return self.__longitude

    @property
    def weather_language(self):
        return self.__weather_language

    @property
    def weather_unit(self):
        return self.__weather_unit

    @property
    def weather_api_token(self):
        return self.__weather_api_token

    @property
    def location_api_token(self):
        return self.__location_api_token

    @property
    def feed_url(self):
        return self.__feed_url

    @property
    def format_24H(self):
        return self.__24H_format
