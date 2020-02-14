import unittest
from unittest.mock import patch, Mock

from project.game import ScoreBlock

mock_input = Mock()

@patch('builtins.input', create=True, new=mock_input)
class TestScoreBlock(unittest.TestCase):

    def setUp(self):
        self.scoreblock = ScoreBlock()

    def test_verify_score(self):
        score = self.scoreblock._verify_score(18, 3)

        self.assertEqual(18, score)

    def test_verify_score_to_low(self):
        with self.assertRaises(Exception) as e:
            self.scoreblock._verify_score(2, 6)

        self.assertEqual('invalid score', str(e.exception))

    def test_verify_score_to_high(self):
        with self.assertRaises(Exception) as e:
            self.scoreblock._verify_score(7, 1)

        self.assertEqual('invalid score', str(e.exception))

    def test_verify_score_invalid(self):
        with self.assertRaises(Exception) as e:
            self.scoreblock._verify_score(11, 3)

        self.assertEqual('invalid score', str(e.exception))

    def test_total_score(self):
        self.scoreblock.ones = 3
        self.scoreblock.twos = 6
        self.scoreblock.threes = 6
        self.scoreblock.fours = 8
        self.scoreblock.fives = 10
        self.scoreblock.sixs = 6

        total_score = self.scoreblock.total_score()

        self.assertEqual(39, total_score)

    def test_total_score_missing(self):
        mock_input.side_effect = ['y']
        self.scoreblock.twos = 6
        self.scoreblock.threes = 6
        self.scoreblock.fours = 8
        self.scoreblock.fives = 10
        self.scoreblock.sixs = 6

        total_score = self.scoreblock.total_score()

        self.assertEqual(36, total_score)

    def test_total_score_missing_error(self):
        mock_input.side_effect = ['n']
        self.scoreblock.twos = 6
        self.scoreblock.threes = 6
        self.scoreblock.fours = 8
        self.scoreblock.fives = 10
        self.scoreblock.sixs = 6

        with self.assertRaises(TypeError):
            self.scoreblock.total_score()
