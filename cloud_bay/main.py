# -*- coding: utf-8 -*-
""" main module controller
    ~~~~~~~~~~~~~~~~
"""
import sys
import click

from market_factory import MarketFactory
from config_yml_parser import ParseYml
from config import ConfigFactory


def main(only_show_price, config_file_name):
    """
    Main command-line execution loop.
    """
    try:
        if "" != str(config_file_name):
            parser = ParseYml()
            config = ConfigFactory(parser, config_file_name)
            market = MarketFactory().get_market(config)

            if True is only_show_price:
                print(market.name, market.prices())
            else:
                print("start some instance")
                print(config.node_spec[0])
                print(config.node_spec[1])

    except BaseException as e:
        print("something going wrong\n%s" % e)

    sys.exit(0)


@click.command()
@click.help_option('-h', '-help')
@click.option('--config', default='configs/project1.yml', help='what to do and where =).')
@click.option('--only-price', is_flag=True, help='Show cloud node price (provider depends on config).')
def get_cli_args(config, only_price, help=0):
    """
       Parse CLI Arguments
       ( default config 'configs/project1.yml' )
    """
    if None is not help:
        click.help_option()
    main(only_price, config)


if __name__ == '__main__':
    get_cli_args()
