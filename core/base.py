"""
Test Core Class
"""
import logging

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Fish(object):

    def __init__(self, ftype):
        self.type = ftype

    def swim(self):
        logger.info("%s fish!", self.type)
