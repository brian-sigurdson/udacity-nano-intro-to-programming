import Player
import random


class RandomPlayer(Player):
    def move(self):
        return random.choice(self.moves)