
from config_aws_parser import ConfigAws


class ConfigFactory(object):

    _config = []
    _parser = None
    _provider_name = None
    _provider = None

    def __init__(self, parser, filename):
        self._parser = parser
        self._filename = filename

        self._config = self._parser.parse(filename)
        self._provider_name = self._config['plan'].keys()[0]

        if "aws" == self._provider_name:
            self._provider = ConfigAws
        else:
            self._provider = ConfigAws

    @property
    def values(self):
        return self._config

    @values.setter
    def values(self, config):
        self._config = config

    # def cloud_provider_name(self):
    #     return self._provider_name

    def __getattr__(self, name):
        if None is not self._provider_name:
            return getattr(self._provider, name)(self._config['plan'][self._provider_name])
        else:
            return None
