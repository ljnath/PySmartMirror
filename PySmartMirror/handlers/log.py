import logging
from logging.handlers import TimedRotatingFileHandler

from PySmartMirror.common.singleton import Singleton


class LogHandler(metaclass=Singleton):
    def get_logger(self, name='pysmartmirror'):
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
