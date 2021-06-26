import time
from tkinter import TOP, E, Frame, Label

from PySmartMirror.handlers.environment import Environment


class Clock(Frame):
    """
    Clock class for creating the clock on TOP-RIGHT of the screen.
    Automatically calls the tick method to update the clock date, day and time.
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.__env = Environment()

        # settting background of widget as background_color
        self.config(bg=self.__env.background_color)

        # default text for date, day and time is loading...
        self.__time = self.__day = self.__date = 'loading...'

        # creating time label
        self.__lb_current_time_text = Label(self, font=(self.__env.font, self.__env.font_size_xl), fg=self.__env.foreground_color, bg=self.__env.background_color)
        self.__lb_current_time_text.pack(side=TOP, anchor=E)

        # creating day label
        self.__lb_current_day_text = Label(self, font=(self.__env.font, self.__env.font_size_m), fg=self.__env.foreground_color, bg=self.__env.background_color)
        self.__lb_current_day_text.pack(side=TOP, anchor=E)

        # creating date label
        self.__lb_current_date_text = Label(self, font=(self.__env.font, self.__env.font_size_m), fg=self.__env.foreground_color, bg=self.__env.background_color)
        self.__lb_current_date_text.pack(side=TOP, anchor=E)

        self.__update()

    def __update(self):
        """
        tick method to update clock's date, time and day.
        """
        current_time = time.strftime('%I:%M:%S %p' if not self.__env.format_24H else '%H:%M')
        current_day = time.strftime('%A')
        current_date = time.strftime('%b %d, %Y')

        # if time string has changed, update it
        if current_time != self.__time:
            self.__time = current_time
            self.__lb_current_time_text.config(text=self.__time)

        # if day has changed, update it
        if current_day != self.__day:
            self.__day = current_day
            self.__lb_current_day_text.config(text=self.__day)

        # if date has changed, update it
        if current_date != self.__date:
            self.__date = current_date
            self.__lb_current_date_text.config(text=self.__date)

        # calls itself every 200 ms
        self.after(500, lambda: self.__update())
