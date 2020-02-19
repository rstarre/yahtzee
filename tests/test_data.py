class TestData:
    class Player:
        def __init__(self, name):
            self.name = name
            self.scoreblock = self.ScoreBlock()

        class ScoreBlock:
            def total_score(self):
                return 10

            def ones(self):
                pass

            def twos(self):
                pass

            def threes(self):
                pass

            def fours(self):
                pass

            def fives(self):
                pass

            def sixs(self):
                pass

    class Round:
        def __init__(self, *args):
            self.args = args
            self.dices = ["dice1", "dice2", "dice3"]

        def throw(self):
            pass

    class TestDice:
        def __init__(self):
            self.roll_called = False

        def roll(self):
            self.roll_called = True
            pass
