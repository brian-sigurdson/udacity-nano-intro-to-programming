import random
import time
import adventure_game_inputs


def print_pause(message):
    print(message)
    time.sleep(1)


def validate_input(prompt, options):
    while True:
        input_response = input(prompt).lower()

        for option in options:
            if option in input_response:
                return option

        print_pause(f"Sorry, I don't understand your response: "
                    f"{input_response}\n")


def present_house_cave_menu():
    return (
        "Enter 1 to knock on the door of the house.\n"
        "Enter 2 to peer into the cave.\n"
        "Enter 3 to quit.\n"
        "What would you like to do?  (1, 2, or 3)\n"
    )


def present_fight_flight_menu():
    return (
        "\nEnter 1 to fight.\n"
        "Enter 2 to run.\n"
        "Enter 3 to quit.\n"
        "What would you like to do?  (1, 2, or 3)\n"
    )


def present_play_again_menu():
    return (
        "\nEnter 1 to play another game.\n"
        "Enter 2 to quit.\n"
        "What would you like to do?  (1 or 2)\n"
    )


def intro(normal_weapon, monster):
    print()
    print_pause("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.")
    print_pause(
        f"Rumor has it that a wicked {monster} is somewhere around here, and "
        f"has been terrifying the nearby village."
    )
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause(f"In your hand you hold your trusty {normal_weapon}.\n")
    return validate_input(present_house_cave_menu(), ["1", "2", "3"])


def fight(arsenal, super_weapon, normal_weapon, monster):
    print()
    print_pause(f"The {monster} attacks, and you attack with your "
                f"{normal_weapon}.")

    if super_weapon in arsenal:
        print_pause(f"You remember that you have a {super_weapon} in your "
                    f"arsenal.")
        print_pause(f"You reveal your {super_weapon}.  The {monster} sees it.")
        print_pause(f"The {monster} shrieks with fear and runs away.")
        print_pause(f"Congratulations!  You win the game!")
    else:
        print_pause(f"You wish you had a {super_weapon}, but you only have "
                    f"your {normal_weapon}.")
        print_pause(f"Unfortunately, your {normal_weapon} is no match for "
                    f"the {monster}.")
        print_pause("Sorry.  You lose.")


def cave(arsenal, super_weapon, normal_weapon):
    print()
    print_pause("You enter the cave.")
    print_pause("You see a powerful weapon.")

    if super_weapon not in arsenal:
        print_pause(f"'A {super_weapon}!'")
        print_pause(f"'Lucky me! Now, I have a {normal_weapon} and a"
                    f" {super_weapon}.'")
        arsenal.append(super_weapon)
    else:
        print_pause(f"Aww.  That is just a {super_weapon}.  I already have "
                    f"a {super_weapon} in my arsenal.")

    return field()


def field():
    print()
    print_pause("You walk out into the field")
    return validate_input(present_house_cave_menu(), ["1", "2", "3"])


def house(arsenal, super_weapon, normal_weapon, monster):
    print()
    print_pause("You walk up to the house.")
    print_pause("You knock on the door of the house.")
    print_pause(f"A fearsome {monster} answers the door.")
    print_pause(f"The {monster} is about to attack.")
    print_pause("What are you going to do?")

    user_choice = validate_input(present_fight_flight_menu(), ["1", "2", "3"])

    if user_choice == "1":
        # the game is won or lost in this function
        fight(arsenal, super_weapon, normal_weapon, monster)
        return "4"
    elif user_choice == "2":
        # user chose not to fight
        return field()
    else:
        # user chose to quit the game
        return "3"


def main():
    play_game = True
    game_won_or_lost = False
    player_quit = False

    while play_game:
        arsenal = []
        normal_weapon = random.choice(adventure_game_inputs.weapons)
        super_weapon = random.choice(adventure_game_inputs.weapons)
        monster = random.choice(adventure_game_inputs.monsters)
        player_choice = intro(normal_weapon, monster)

        while True:
            if player_choice == "1":
                player_choice = house(arsenal, super_weapon, normal_weapon,
                                      monster)
            elif player_choice == "2":
                player_choice = cave(arsenal, super_weapon, normal_weapon)
            elif player_choice == "4":
                # game was won or lost
                game_won_or_lost = True
                break
            else:
                # player wants to quit
                player_quit = True
                game_won_or_lost = False
                play_game = False
                break

        if game_won_or_lost:
            # play again?
            player_choice = validate_input(present_play_again_menu(),
                                           ["1", "2"])
            if player_choice == "1":
                continue
            else:
                player_quit = True
                play_game = False

        if player_quit:
            play_game = False

    print_pause("Good-bye!")


main()
