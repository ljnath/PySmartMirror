import logging
from logging.handlers import TimedRotatingFileHandler

from PySmartMirror.common.singleton import Singleton


class LogHandler(metaclass=Singleton):
    """
    Singleton class for handling logs in this project
    """

    def get_logger(self, name='pysmartmirror'):
        """
        Method to return a logger based on the name that user has specifed; default is pysmartmirror
        It will check if the logger is already present, if yes it will return that, else it will create a new one and return it.
        The File logger is configured to rotate daily.
        param name:str Name of logger
        """
        logger = logging.getLogger(name)
        log_formatter = logging.Formatter('%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        logger.setLevel(logging.INFO)

        if not logger.hasHandlers():
            console_log_handler = logging.StreamHandler()
            console_log_handler.setFormatter(log_formatter)
            logger.addHandler(console_log_handler)

            file_log_handler = TimedRotatingFileHandler(filename=f'{name}.log', when="midnight", interval=1)
            file_log_handler.setFormatter(log_formatter)
            logger.addHandler(file_log_handler)
        return logger
