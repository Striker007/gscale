
from market_aws import MarketAws


class MarketFactory(object):
    """
    Market Factory
    """
    market = None

    def get_market(self, config):

        if 'aws' == config.cloud_provider_name:
            self.market = MarketAws(config.secrets['access_key_id'], config.secrets['secret_access_key'])
        else:
            self.market = MarketAws(config.secrets['access_key_id'], config.secrets['secret_access_key'])

        return self.market
