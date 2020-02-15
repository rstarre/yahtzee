import unittest
from unittest.mock import patch, Mock

from .test_data import TestData
from project.game import Round, Player


class TestRound(unittest.TestCase):

    def setUp(self):
        with patch('project.game.Dice', return_value=TestData.TestDice()) as mock_dice:
            self.round = Round(6)

        self.round.nr_dices = 6

    def test_init(self):
        self.assertEqual(3, self.round.throws)
        self.assertIsInstance(self.round.score, list)
        self.assertEqual(6, self.round.nr_dices)
        self.assertEqual(6, len(self.round.dices))
        self.assertIsInstance(self.round.dices[1], TestData.TestDice)

    def test_throw(self):
        self.round.throw()

        self.assertEqual(2, self.round.throws)

        for dice in self.round.dices:
            self.assertTrue(dice.roll_called)

    @patch('builtins.print')
    def test_throw_no_more(self, mock_print):
        self.round.throws = 0

        self.round.throw()

        mock_print.assert_called_with("No more throws allowed.")

    def test_select_dice(self):
        self.round.select_dice('2')

        self.assertEqual(1, len(self.round.score))
        self.assertEqual(5, len(self.round.dices))

    def test_write_score(self):
        #TODO
        pass












