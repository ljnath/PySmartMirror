"""
MIT License

Copyright (c) 2021 Lakhya Jyoti Nath

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

PySmartMirror - SmartMirror project written in python3
Version: 1.0.0
Author: Lakhya Jyoti Nath (ljnath)
Email:  ljnath@ljnath.com
Website: https://www.ljnath.com
"""


from tkinter import BOTH, BOTTOM, LEFT, RIGHT, TOP, YES, Frame, N, S, Tk

from PySmartMirror.handlers.config import ConfigHandler
from PySmartMirror.handlers.environment import Environment
from PySmartMirror.widgets.clock import Clock
from PySmartMirror.widgets.feeds import Feeds
from PySmartMirror.widgets.weather import Weather


class SmartMirror:
    """
    Main SmartMirror class which loads user configurations, creates mirror and adds widgets to it
    """
    def __init__(self, config_file):
        # initializing ConfigHandler and loading all the configuration into a dict
        config_handler = ConfigHandler(config_file)
        configs = config_handler.load()

        # initilaizing Environment and populating all environment variabled with user configurations
        env = Environment()
        env.populate(configs)

        # creating tkinter window with background color as black
        self.__tkinter = Tk()
        self.__tkinter.configure(background=env.background_color)

        # creating 3 frames - TOP, CENTER, BOTTOM
        self.top_frame = Frame(self.__tkinter, background=env.background_color)
        self.center_frame = Frame(self.__tkinter, background=env.background_color)
        self.bottom_frame = Frame(self.__tkinter, background=env.background_color)

        # positioning the frames
        self.top_frame.pack(side=TOP, fill=BOTH, expand=YES)
        self.center_frame.pack(side=TOP, fill=BOTH, expand=YES)
        self.bottom_frame.pack(side=BOTTOM, fill=BOTH, expand=YES)

        # setting default fullscreen switch to false
        self.__is_fullscreen = False

        # binding keyboard keys [ENTER] and [ESCAPE] to enable fullscreen and end fullscreen
        self.__tkinter.bind("<Return>", self.toggle_fullscreen)
        self.__tkinter.bind("<Escape>", self.end_fullscreen)

        # creating and adding clock widget
        clock_widget = Clock(parent=self.top_frame)
        clock_widget.pack(side=RIGHT, anchor=N, padx=40, pady=60)

        # creating and adding weather widget
        weather_widget = Weather(self.top_frame)
        weather_widget.pack(side=LEFT, anchor=N, padx=40, pady=60)

        # creating and adding feed widget
        feeds_widget = Feeds(self.bottom_frame)
        feeds_widget.pack(side=LEFT, anchor=S, padx=40, pady=40)

    def start(self, fullscreen: bool) -> None:
        """
        Method to start the smart mirror
        """
        if fullscreen:
            self.__tkinter.attributes("-fullscreen", True)
        self.__tkinter.mainloop()

    def toggle_fullscreen(self, event=None):
        """
        Method to toggle fullscreen
        """
        self.__is_fullscreen = not self.__is_fullscreen
        self.__tkinter.attributes("-fullscreen", self.__is_fullscreen)
        return "break"

    def end_fullscreen(self, event=None):
        """
        Method to end fullscreen
        """
        self.__is_fullscreen = False
        self.__tkinter.attributes("-fullscreen", False)
        return "break"
