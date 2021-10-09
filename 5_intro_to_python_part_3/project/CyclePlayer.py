import Player
import random


class CyclePlayer(Player.AbstractPlayer):
    def move(self):
        # determine the move by taking the length of the list of
        # my moves modulus the length of the moves list
        # this should always select an index value between
        # zero and len(self.moves) - 1
        return self.moves[len(self.my_moves)%len(self.moves)]
