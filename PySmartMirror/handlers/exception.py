from PySmartMirror.handlers.log import LogHandler


class BaseException(Exception):
    """
    Base Exception class in this project
    """
    def __init__(self, message=None):
        super().__init__()
        self.logger = LogHandler().get_logger()
        if message:
            self.logger.exception(message)


class InvalidInput(BaseException):
    """
    Exception class to be raised when any input is invalid
    """
    def __init__(self, message):
        super().__init__()
        self.logger.exception(message)


class MissingConfiguration(BaseException):
    """
    Exception class raised when any configuration key or value is missing
    """
    def __init__(self, message):
        super().__init__()
        self.logger.exception(message)
