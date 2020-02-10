import unittest
import io
from unittest.mock import patch, Mock
from test_data import TestData
from project.game import Game

mock_input = Mock()


@patch('builtins.input', create=True, new=mock_input)
class GameTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        
    def tearDown(self):
        mock_input.reset_mock()

    @patch('project.game.Player')
    def test_add_user(self, mock_player):
        mock_player.return_value = 'player1'

        self.game.add_player('testq')

        self.assertEqual('player1', self.game.players[0])
        mock_player.assert_called_with('testq')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_play_round_invalid(self, mock_output):
        mock_input.side_effect = ['test', 'exit']
        self.game.add_player('test1')

        self.game.play_round()

        self.assertTrue('invalid option' in mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_play_round_names(self, mock_output):
        mock_input.side_effect = ['exit', 'exit']
        self.game.add_player('test1')
        self.game.add_player('test2')

        self.game.play_round()

        self.assertTrue('it is test1s turn' in mock_output.getvalue())
        self.assertTrue('it is test2s turn' in mock_output.getvalue())

    # @patch('sys.stdout', new_callable=io.StringIO)
    @patch('project.game.Round.throw')
    def test_play_round_throw(self, mock_round):
        mock_input.side_effect = ['throw', 'exit']
        self.game.add_player('test1')

        self.game.play_round()

        mock_round.assert_called()

    @patch('project.game.Round.select_dice')
    def test_play_round_select_dices(self, mock_round):
        mock_input.side_effect = ['select dices', '1 2 3', 'exit']
        self.game.add_player('test1')

        self.game.play_round()

        mock_round.assert_called_with(['1', '2', '3'])
        mock_input.assert_any_call('Which dices do you want to save?')

    @patch('project.game.vars')
    @patch('project.game.Round.write_score')
    def test_play_round_write_score(self, mock_round, mock_scoreblock_vars):
        mock_input.side_effect = ['write score', 'key1', 'exit']
        mock_scoreblock_vars.return_value = {'key1': 'test', 'key2': 'test2'}
        self.game.add_player('test1')

        self.game.play_round()

        mock_round.assert_called_with(self.game.players[0], 'key1')
        mock_input.assert_any_call("Where do you want to write your scores? (['test', 'test2'])")

    @patch('builtins.print')
    def test_play_round_exit(self, mock_output):
        mock_input.side_effect = ['exit']
        self.game.add_player('test1')

        self.game.play_round()

        mock_output.assert_called_with('End of the round')
    
    @patch('project.game.Game.play_round')
    @patch('project.game.Game.add_player')
    @patch('builtins.print')
    def test_play_game_0_rounds_1_player(self, mock_print, mock_player, mock_round):
        mock_input.side_effect = ['1', 'test1']
        player1 = TestData.Player('player1')
        self.game.players = [player1]
        self.game.rounds = 0
        
        self.game.play_game()

        mock_input.assert_any_call('Welcome to Yathzee!! \n With how many people will you play this game?')
        mock_input.assert_any_call('What is the name of player 1?')
        self.assertEqual(player1.name, self.game.players[0].name)
        mock_player.assert_any_call('test1')
        mock_print.assert_called_with(f'{player1.name} has a score of {player1.scoreblock.total_score()}')
        self.assertEqual(0, mock_round.call_count)

    @patch('project.game.Game.play_round')
    @patch('project.game.Game.add_player')
    @patch('builtins.print')
    def test_play_game_4_rounds_1_player(self, mock_print, mock_player, mock_round):
        mock_input.side_effect = ['1', 'test1']
        player1 = TestData.Player('player1')
        self.game.players = [player1]
        self.game.rounds = 4

        self.game.play_game()

        mock_input.assert_any_call('Welcome to Yathzee!! \n With how many people will you play this game?')
        mock_input.assert_any_call('What is the name of player 1?')
        self.assertEqual(player1.name, self.game.players[0].name)
        mock_player.assert_any_call('test1')
        mock_print.assert_called_with(f'{player1.name} has a score of {player1.scoreblock.total_score()}')
        self.assertEqual(4, mock_round.call_count)

    @patch('project.game.Game.play_round')
    @patch('project.game.Game.add_player')
    @patch('builtins.print')
    def test_play_game_4_rounds_2_player(self, mock_print, mock_player, mock_round):
        mock_input.side_effect = ['2', 'test1', 'test2']
        player1 = TestData.Player('player1')
        player2 = TestData.Player('player2')
        self.game.players = [player1, player2]
        self.game.rounds = 4

        self.game.play_game()

        mock_input.assert_any_call('Welcome to Yathzee!! \n With how many people will you play this game?')
        mock_input.assert_any_call('What is the name of player 1?')
        self.assertEqual(player1.name, self.game.players[0].name)
        mock_player.assert_any_call('test1')
        mock_player.assert_any_call('test2')
        mock_print.assert_any_call(f'{player1.name} has a score of {player1.scoreblock.total_score()}')
        mock_print.assert_any_call(f'{player2.name} has a score of {player2.scoreblock.total_score()}')
        self.assertEqual(4, mock_round.call_count)

    @patch('project.game.Game.play_round')
    @patch('project.game.Game.add_player')
    @patch('builtins.print')
    def test_play_game_wrong_input(self, mock_print, mock_player, mock_round):
        mock_input.side_effect = ['test', '1', 'test1']
        player1 = TestData.Player('player1')
        self.game.players = [player1]
        self.game.rounds = 0

        self.game.play_game()

        mock_input.assert_any_call('Welcome to Yathzee!! \n With how many people will you play this game?')
        mock_input.assert_any_call('What is the name of player 1?')
        self.assertEqual(player1.name, self.game.players[0].name)
        mock_player.assert_any_call('test1')
        mock_print.assert_called_with(f'{player1.name} has a score of {player1.scoreblock.total_score()}')
        self.assertEqual(0, mock_round.call_count)
        mock_print.assert_any_call("please enter a digit")


if __name__ == '__main__':
    unittest.main()






