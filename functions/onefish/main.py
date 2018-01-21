"""
One Fish
"""
import logging
import requests

import helper
import core.base as base

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def run():
    """Entrypoint"""
    my_ip = requests.get('https://api.ipify.org?format=json')
    logger.info(my_ip.json())
    logger.info(helper.get_uuid())
    fish = base.Fish('Red')
    fish.swim()


def test_me(one, two):
    return one + two


if __name__ == '__main__':
    run()
