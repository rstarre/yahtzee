import unittest
from unittest.mock import patch, Mock
from project.game import Player


class PlayerTest(unittest.TestCase):

    @patch('project.game.ScoreBlock')
    def test_player(self, mock_scoreblock):
        class ScoreBlockTest:
            pass

        mock_scoreblock.return_value = ScoreBlockTest()

        player = Player('test')

        self.assertEqual('test', player.name)
        self.assertTrue(isinstance(player.scoreblock, ScoreBlockTest))
