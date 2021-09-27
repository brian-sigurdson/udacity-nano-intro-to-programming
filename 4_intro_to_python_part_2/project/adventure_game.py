import time


def print_pause(message):
    print(message)
    # time.sleep(1)
    time.sleep(0)


def validate_input(prompt, options):
    while True:
        input_response = input(prompt).lower()

        for option in options:
            if option in input_response:
                return option

        print_pause(f"Sorry, I don't understand your response: {input_response}\n")


def intro():
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause(
        """Rumor has it that a wicked fairy is somewhere around here, and has been terrifying the nearby village."""
    )
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause(f"In your hand you hold your trusty (but not very effective) (something here).\n")
    return validate_input(
        "Enter 1 to knock on the door of the house.\n"
        "Enter 2 to peer into the cave.\n"
        "Enter 3 to quit.\n"
        "What would you like to do?  (1, 2, or 3)\n",
        ["1", "2", "3"]
    )


player_choice = intro()
print("player choose " + player_choice)



