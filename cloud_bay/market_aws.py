
import boto.ec2


from market import Market


class MarketAws(Market):

    _access_key = ""
    _secret_access_key = ""
    name = "aws"
    region = "eu-central-1"
    TYPE = "Linux/UNIX (Amazon VPC)"
    # instanceType = 'c4.4xlarge'
    # instanceType = 'm4.4xlarge'
    instanceType = 'c3.2xlarge'
    aZ = "eu-central-1a"

    def __init__(self, access_key, secret_access_key):
        self._access_key = access_key
        self._secret_access_key = secret_access_key

    def prices(self):

        ec = boto.ec2.connect_to_region(self.region,
                                        aws_access_key_id=self._access_key,
                                        aws_secret_access_key=self._secret_access_key)

        prices = ec.get_spot_price_history(instance_type=self.instanceType,
                                           product_description=self.TYPE, availability_zone=self.aZ)

        ec.get_all_spot_instance_requests()

        price = 0.0
        # for tm in [0, 1, 2, 3, 4]:
        #     price += float(prices[tm].price)
        i = 0
        for p in prices:
            i += 1
            price += p.price

        print(prices[5], type(prices[8]))

        return round(float(price) / i, 3), round(float(prices[0].price), 3)
