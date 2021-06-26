from PySmartMirror.models.location import Location


class Weather:
    """
    Weather model class
    """
    def __init__(self):
        self.__temperature = ''
        self.__current_state = ''
        self.__forecast = ''
        self.__location = Location()
        self.__icon_text = ''
        self.__image = ''

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        self.__temperature = value

    @property
    def current_state(self):
        return self.__current_state

    @current_state.setter
    def current_state(self, value):
        self.__current_state = value

    @property
    def forecast(self):
        return self.__forecast

    @forecast.setter
    def forecast(self, value):
        self.__forecast = value

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        self.__location = value

    @property
    def icon_text(self):
        return self.__icon_text

    @icon_text.setter
    def icon_text(self, value):
        self.__icon_text = value

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, value):
        self.__image = value
