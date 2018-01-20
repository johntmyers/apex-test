"""
Tests
"""
import pytest
import unittest

from functions.onefish import main


class BaseTest(unittest.TestCase):
    '''Tests for Request'''

    def setUp(self):
        pass

    def test_test_me(self):
        self.assertEquals(5, main.test_me(2, 3))
