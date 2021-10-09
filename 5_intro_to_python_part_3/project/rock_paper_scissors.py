#!/usr/bin/env python3

import RandomPlayer
import HumanPlayer
import ReflectPlayer
import CyclePlayer

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""


class Game:
    def __init__(self, p1, p2, max_rounds):
        self.p1 = p1
        self.p2 = p2
        self.max_rounds = max_rounds
        self.current_round = 0
        # winner is relative to player p1, see the beats function for details
        self.round_winner = []

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        print(f"Player 1: {move1}  Player 2: {move2}")
        result = self.beats(move1, move2)
        self.round_winner.append(result)

        if result == 1:
            print("Player 1 wins!")
        elif result == 0:
            print("The round is a tie!")
        else:
            print("Player 2 wins!")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for current_round in range(self.max_rounds):
            print(f"Round {current_round + 1}:")
            self.play_round()
            print()
        print("Game over!\n")
        self.announce_round_winners()
        print()
        self.announce_overall_winner()

    def announce_round_winners(self):
        print("Results by Round")
        print("---------------------------")
        for current_round in range(self.max_rounds):
            print(f"Round {current_round +1} winner: " +
                  self.get_round_winner_name(current_round))

    def announce_overall_winner(self):
        player_1 = self.round_winner.count(1)
        player_2 = self.round_winner.count(-1)
        if player_1 == player_2:
            print("The players have tied.")
        elif player_1 > player_2:
            print(f"Player 1 is the winner, with {player_1} wins.")
        else:
            print(f"Player 2 is the winner, with {player_2} wins.")

    def get_round_winner_name(self, game_round):
        if self.round_winner[game_round] == 1:
            return "Player 1"
        elif self.round_winner[game_round] == 0:
            return "Tie / No winner"
        else:
            return "Player 2"

    def beats(self, one, two):
        if one == two:
            return 0
        else:
            # winning is in reference to object one.
            # return false => one lost
            # rock beats scissors, scissors beats paper, paper beats rock
            result = ((one == 'rock' and two == 'scissors') or
                    (one == 'scissors' and two == 'paper') or
                    (one == 'paper' and two == 'rock'))
            if result:
                return 1
            else:
                return -1


if __name__ == '__main__':
    while True:
        try:
            num_rounds = int(input("How many rounds would you like to play?  "
                                   "eg. 1 or 2 or 3 or ... or 0 to quit\n"))
            if num_rounds == 0:
                break
            else:
                game = Game(HumanPlayer.HumanPlayer(),
                            RandomPlayer.RandomPlayer(), num_rounds)
                game.play_game()
                break
        except ValueError:
            print("Please enter an integer value.")

