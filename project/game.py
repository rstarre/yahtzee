import random


class Game:

    def __init__(self):
        self.players = []
        self.nr_dices = 6
        self.round = Round(self.nr_dices)
        self.rounds = len(ScoreBlock.nr_of_boxes())

    def add_player(self, name):
        self.players.append(Player(name))

    def play_round(self):
        for player in self.players:
            print(f'it is {player.name}s turn')
            while True:
                action = input("select a action: 'throw', 'select dices', 'write score'.")
                if 'throw' == action.lower():
                    self.round.throw()
                    [print(dice.value) for dice in self.round.dices]
                elif 'select dices' == action.lower():
                    index = input("Which dices do you want to save?").lower().split()
                    print(index)
                    self.round.select_dice(index)
                elif 'write score' == action.lower():
                    score = input(f"Where do you want to write your scores? ({list(vars(ScoreBlock()).values())})")
                    self.round.write_score(player, score)
                    break
                elif 'exit' == action.lower():
                    break
                else:
                    print('invalid option')
        else:
            print('End of the round')

    def play_game(self):
        while True:
            nr_of_players = input('Welcome to Yathzee!! \n With how many people will you play this game?')
            try:
                for i in range(int(nr_of_players)):
                    name = input(f"What is the name of player {i+1}?")
                    self.add_player(name)
            except Exception as e:
                print("please enter a digit")
            else:
                break

        for _ in range(self.rounds):
            self.play_round()
        else:
            print('end of the game!')

        for player in self.players:
            print(f'{player.name} has a score of {player.scoreblock.total_score()}')


class Player:

    def __init__(self, name):
        self.name = name
        self.scoreblock = ScoreBlock()


class ScoreBlock:

    def __init__(self):
        self._ones = None
        self._twos = None
        self._threes = None
        self._fours = None
        self._fives = None
        self._sixs = None

    def _verify_score(self, score, number):
        if number <= score <= (6*number) and score % number == 0:
            return score
        else:
            raise Exception('invalid score')

    def total_score(self):
        scores = vars(self)
        total_score = 0

        for key, score in scores.items():
            try:
                total_score += int(score)
            except TypeError as e:
                cont = input(f'There is no score for {key}, skip score? (y/n)')
                if cont.lower() == 'y':
                    pass
                else:
                    raise
        return total_score

    @staticmethod
    def nr_of_boxes():
        return vars(ScoreBlock())

    @property
    def ones(self):
        return self._ones

    @ones.setter
    def ones(self, score):
        self._ones = self._verify_score(score, 1)

    @property
    def twos(self):
        return self._twos

    @twos.setter
    def twos(self, score):
        self._twos = self._verify_score(score, 2)

    @property
    def threes(self):
        return self._threes

    @threes.setter
    def threes(self, score):
        self._threes = self._verify_score(score, 3)

    @property
    def fours(self):
        return self._fours

    @fours.setter
    def fours(self, score):
        self._fours = self._verify_score(score, 4)
            
    @property
    def fives(self):
        return self._fives

    @fives.setter
    def fives(self, score):
        self._fives = self._verify_score(score, 5)
            
    @property
    def sixs(self):
        return self._sixs

    @sixs.setter
    def sixs(self, score):
        self._sixs = self._verify_score(score, 6)


class Round:

    def __init__(self, nr_dices):
        self.score = []
        self.throws = 3
        self.nr_dices = nr_dices
        self.dices = [Dice() for _ in range(nr_dices)]

    def throw(self):
        if self.throws > 0:
            [dice.roll() for dice in self.dices]
            self.throws -= 1
        else:
            print("No more throws allowed.")

    def select_dice(self, index):
        for index in index:
            self.score.append(self.dices.pop(int(index)))

    def write_score(self, player, score):
        #TODO
        pass



class Dice:

    def __init__(self):
        self.value = None

    def roll(self):
        self.value = random.randint(1, 6)

    def reset(self):
        self.value = None






if __name__ == '__main__':
    x = Game()
    x.play_game()


    # print(x.dices)
    # x.throw()
    # print(x.dices[0].value)