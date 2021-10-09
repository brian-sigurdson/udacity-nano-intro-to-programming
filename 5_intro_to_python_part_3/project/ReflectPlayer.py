import Player
import random


class ReflectPlayer(Player.AbstractPlayer):
    def move(self):
        if len(self.their_moves) == 0:
            # first round, just choose a random move
            return random.choice(self.moves)
        else:
            # choose the move my opponent chose last round
            return self.their_moves[-1]
