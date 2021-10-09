import Player


class HumanPlayer(Player.AbstractPlayer):
    def move(self):
        while True:
            choice = \
                input("Please enter your move:  "
                      "rock, paper, scissors\n").lower()

            if choice in self.moves:
                return choice
            else:
                print(f"I'm sorry, but {choice} is an invalid choice.")
                print("Please enter again.")
