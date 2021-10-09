import Player
import random


class RandomPlayer(Player.AbstractPlayer):
    def move(self):
        return random.choice(self.moves)
