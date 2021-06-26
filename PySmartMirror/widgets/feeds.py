from tkinter import LEFT, TOP, Frame, Label, N, W

from PIL import Image, ImageTk
from PySmartMirror.handlers.environment import Environment
from PySmartMirror.handlers.network import NetworkHandler
from PySmartMirror.handlers.log import LogHandler


class Feeds(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent)

        self.__env = Environment()
        self.__logger = LogHandler().get_logger()

        self.config(background=self.__env.background_color)

        self.__lb_feed_header = Label(self, text='loading...', font=(self.__env.font, self.__env.font_size_m), fg=self.__env.foreground_color, bg=self.__env.background_color)
        self.__lb_feed_header.pack(side=TOP, anchor=W)

        self.__frame_feeds = Frame(self, bg=self.__env.background_color)
        self.__frame_feeds.pack(side=TOP)

        # checking for news feed 2s after app load-up
        self.after(2 * 1000, self.__update)

    def __update(self):
        self.__lb_feed_header.config(text='Top global headlines')

        try:
            # remove existing feeds
            for widget in self.__frame_feeds.winfo_children():
                widget.destroy()

            updated_feeds = NetworkHandler().get_feeds_from_google(self.__env.feed_url)

            # adding new feeds to frame
            for feed in updated_feeds:
                headline = FeedsFrame(self.__frame_feeds, f' {feed}')
                headline.pack(side=TOP, anchor=W)

        except Exception as e:
            self.__logger.error('Failed to update feeds')
            self.__logger.exception(e, exc_info=True)

        # updating needs feeds every 10s
        self.after(10 * 1000, lambda: self.__update)


class FeedsFrame(Frame):
    def __init__(self, parent, feed_title):
        super().__init__(parent)

        self.__env = Environment()
        self.config(bg=self.__env.background_color)

        feed_image = self.__env.get_image_path('feeds')

        if feed_image:
            feed_image = Image.open(feed_image)
            feed_image = feed_image.resize((25, 25), Image.ANTIALIAS)
            feed_image = feed_image.convert('RGB')
            feed_photo = ImageTk.PhotoImage(feed_image)

            lb_feed_icon = Label(self, bg=self.__env.background_color, image=feed_photo)
            lb_feed_icon.image = feed_photo
            lb_feed_icon.pack(side=LEFT, anchor=N)

        lb_feed_title = Label(self, text=feed_title, font=(self.__env.font, self.__env.font_size_s), fg=self.__env.foreground_color, bg=self.__env.background_color)
        lb_feed_title.pack(side=LEFT, anchor=N)
