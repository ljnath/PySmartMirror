import json
import os

from PySmartMirror.handlers.exception import InvalidInput, MissingConfiguration
from PySmartMirror.handlers.log import LogHandler


class ConfigHandler:
    def __init__(self, config_file):
        self.__logger = LogHandler().get_logger()
        self.__config_file = config_file

        if not self.__config_file:
            raise InvalidInput('Input configuation file cannot be empty')

        if not os.path.exists(self.__config_file):
            raise InvalidInput(f'Input configuation file {self.__config_file} is missing')

        if not os.path.isfile(self.__config_file):
            raise InvalidInput(f'Input configuation file {self.__config_file} is not a file')

    def load(self):
        self.__logger.info(f'Loading configurations from {self.__config_file}')
        json_configs = {}
        with open(self.__config_file) as json_data_file:
            json_configs = json.load(json_data_file)
        self.__validate(json_configs)
        return json_configs

    def __validate(self, json_configs):
        self.__logger.debug('Validation configurations')

        expected_keys = (
            'locale',
            'unit',
            'feed_url',
            'font_family',
            '24H_format',
            'font_size',
            ('font_size', 'xl'),
            ('font_size', 'l'),
            ('font_size', 'm'),
            ('font_size', 's'),
            'color',
            ('color', 'background'),
            ('color', 'foreground'),
            'location',
            ('location', 'latitude'),
            ('location', 'longitude'),
            'api_key',
            ('api_key', 'darksky.net'),
            ('api_key', 'opencagedata.com')
        )

        for key in expected_keys:
            local_config = json_configs
            local_key = key

            if type(key) == tuple:
                parent_key, local_key = key
                local_config = json_configs[parent_key]

            if local_key not in local_config.keys():
                raise MissingConfiguration(f'Missing configuration key: {local_key}')
            elif local_config[local_key] is None:
                raise MissingConfiguration(f'Missing configuration value for key: {local_key}')
