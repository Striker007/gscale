import yaml
import logging
import sys
import os
import datetime


__title__ = 'config_yml_parser'


start_time = datetime.datetime.now().strftime('%Y%m%d_%H:%M:%S')
logger = logging.getLogger(__title__)
logger.setLevel(logging.INFO)
ch = logging.FileHandler('{path}/logs/{appname}-{ts}.log'.format(path=os.getcwd(), appname=__title__, ts=start_time))
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

proxy_record_types = ['A', 'CNAME', 'AAAA']
mx_record_types = ['MX']
cfapi_call_counter = 0


class ParseYml(object):

    filename = ""
    values = []

    def parse(self, filename):

        if not filename:
            msg = 'Config file was not set. Please set config file name.'
            logger.critical(msg)
            print(msg)
            sys.exit(1)
        with open(filename, 'r') as f:
            try:
                cfg = yaml.load(f)
            except BaseException as e:
                logger.critical(e)
                raise

        self.values = cfg
        return self.values
