import unittest

from unittest.mock import patch

from project.game import Dice


class TestDice(unittest.TestCase):
    def setUp(self):
        self.dice = Dice()

    def test_roll(self):
        self.dice.roll()

        self.assertIsInstance(self.dice.value, int)

    def test_reset(self):
        self.dice.roll()
        self.assertIsInstance(self.dice.value, int)

        self.dice.reset()

        self.assertIsNone(self.dice.value)
