from PySmartMirror.handlers.log import LogHandler


class BaseException(Exception):
    def __init__(self, message=None):
        super().__init__()
        self.logger = LogHandler().get_logger()
        if message:
            self.logger.exception(message)


class InvalidInput(BaseException):
    def __init__(self, message):
        super.__init__()
        self.logger.exception(message)


class MissingConfiguration(BaseException):
    def __init__(self, message):
        super().__init__()
        self.logger.exception(message)
