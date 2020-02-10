
class TestData:

    class Player:

        def __init__(self, name):
            self.name = name
            self.scoreblock = self.ScoreBlock()

        class ScoreBlock:

            def total_score(self):
                return 10

    class Round:

        def __init__(self, *args):
            self.args = args
            self.dices = ['dice1', 'dice2', 'dice3']

        def throw(self):
            pass