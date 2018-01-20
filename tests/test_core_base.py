"""
Tests
"""
import pytest
import unittest

from core import base


class BaseTest(unittest.TestCase):
    '''Tests for Request'''

    def setUp(self):
        pass

    def test_fish(self):
        fish = base.Fish('Red')
        self.assertEquals(fish.type, 'Red')
