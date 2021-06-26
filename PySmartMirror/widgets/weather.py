from tkinter import LEFT, TOP, Frame, Label, N, W

from PIL import Image, ImageTk
from PySmartMirror.handlers.environment import Environment
from PySmartMirror.handlers.log import LogHandler
from PySmartMirror.handlers.network import NetworkHandler


class Weather(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.__env = Environment()
        self.__logger = LogHandler().get_logger()

        self.config(bg=self.__env.background_color)

        self.__temperature = ''
        self.__forecast = ''
        self.__location = ''
        self.__current_state = ''
        self.__weather_image = ''

        frame_for_temperature = Frame(self, bg=self.__env.background_color)
        frame_for_temperature.pack(side=TOP, anchor=W)

        self.__lb_temperature_value = Label(frame_for_temperature, font=(self.__env.font, self.__env.font_size_xl), fg=self.__env.foreground_color, bg=self.__env.background_color)
        self.__lb_temperature_value.pack(side=LEFT, anchor=N)

        self.__lb_weather_icon = Label(frame_for_temperature, bg=self.__env.background_color)
        self.__lb_weather_icon.pack(side=LEFT, anchor=N, padx=20)

        self.__lb_location = Label(self, font=(self.__env.font, self.__env.font_size_l), fg=self.__env.foreground_color, bg=self.__env.background_color)
        self.__lb_location.pack(side=TOP, anchor=W)

        self.__lb_current_state = Label(self, text='loading...', font=(self.__env.font, self.__env.font_size_m), fg=self.__env.foreground_color, bg=self.__env.background_color)
        self.__lb_current_state.pack(side=TOP, anchor=W)

        self.__lb_forcast = Label(self, font=(self.__env.font, self.__env.font_size_s), fg=self.__env.foreground_color, bg=self.__env.background_color)
        self.__lb_forcast.pack(side=TOP, anchor=W)

        # update weather after 1s
        self.after(1 * 1000, self.__update)

    def __update(self):
        try:
            weather_model = NetworkHandler().get_weather_from_darksky(self.__env.weather_api_token, self.__env.latitude, self.__env.longitude, self.__env.weather_language, self.__env.weather_unit)

            weather_model.location = NetworkHandler().get_location_from_opencage(self.__env.location_api_token, self.__env.latitude, self.__env.longitude)
            weather_model.image = self.__env.get_image_path(weather_model.icon_text)
            location_text = f'{weather_model.location.city}, {weather_model.location.state} {weather_model.location.country_code}'
            degree_sign = u'\N{DEGREE SIGN}'

            # if weather image is available, it is shown
            if weather_model.image and self.__weather_image != weather_model.image:
                self.__weather_image = weather_model.image

                tk_image = Image.open(self.__weather_image)
                tk_image = tk_image.resize((100, 100), Image.ANTIALIAS)
                tk_image = tk_image.convert('RGB')
                weather_photo = ImageTk.PhotoImage(tk_image)

                self.__lb_weather_icon.config(image=weather_photo)
                self.__lb_weather_icon.image = weather_photo
            else:
                # clearing weather image if its not avilable
                self.__lb_weather_icon.config(image='')

            # if temperature value has changed, update it
            if self.__temperature != weather_model.temperature:
                self.__temperature = weather_model.temperature
                self.__lb_temperature_value.config(text=f'{self.__temperature}{degree_sign}c')

            # if current weather status has changed, update it
            if self.__current_state != weather_model.current_state:
                self.__current_state = weather_model.current_state
                self.__lb_current_state.config(text=self.__current_state)

            # if weather forcast has changed, update it
            if self.__forecast != weather_model.forecast:
                self.__forcast = weather_model.forecast
                self.__lb_forcast.config(text=self.__forcast)

            # if location has changed, update it
            if self.__location != location_text:
                self.__location = location_text
                if location_text == ', ':
                    # setting custom text if location value was received but empty
                    self.__location = 'Cannnot Pinpoint Location'
                self.__lb_location.config(text=self.__location)
        except Exception as e:
            self.__logger.error('Failed to update weather')
            self.__logger.exception(e, exc_info=True)

        # auto-updating weather every minute
        self.after(60 * 1000, lambda: self.__update)
