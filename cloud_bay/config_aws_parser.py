
class ConfigAws(object):

    _name = "aws"

    @staticmethod
    def node_spec(config):
        return config['roles']

    @staticmethod
    def cloud_provider_name(config):
        return ConfigAws._name

    @staticmethod
    def secrets(config):
        return config['aws_settings']
