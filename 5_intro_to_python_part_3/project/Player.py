class Player:
    def __init__(self):
        self.moves = ['rock', 'paper', 'scissors']

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    # rock beats scissors
    # paper beats rock
    # scissors beats paper
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))





