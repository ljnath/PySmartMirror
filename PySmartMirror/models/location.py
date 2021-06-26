class Location:
    """
    Location model class with details which will be shown on screen
    """
    def __init__(self):
        self.__city = ''
        self.__state = ''
        self.__country_code = ''

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value

    @property
    def country_code(self):
        return self.__country_code

    @country_code.setter
    def country_code(self, value):
        self.__country_code = value
