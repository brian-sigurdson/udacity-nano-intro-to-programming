class AbstractPlayer:
    """The Player class is the parent class for all of the Players
    in this game"""

    def __init__(self):
        self.moves = ['rock', 'paper', 'scissors']
        self.my_moves = []
        self.their_moves = []

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_moves.append(my_move)
        self.their_moves.append(their_move)

