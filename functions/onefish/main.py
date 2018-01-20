"""
One Fish
"""
import logging
import sys
import os

# look for packages in "lib" directory
sys.path.append(
    os.path.join(os.path.abspath(os.path.dirname(__file__)), 'lib'))

import requests

import helper
import core.base as base

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handle(event, context):
    """Entrypoint"""
    my_ip = requests.get('https://api.ipify.org?format=json')
    logger.info(my_ip.json())
    logger.info(helper.get_uuid())
    fish = base.Fish('Red')
    fish.swim()


def test_me(one, two):
    return one + two
