import time


items = []


def print_pause(msg):
    print(msg)
    time.sleep(1)


def intro():
    print_pause("You have just arrived at your new job!")
    print_pause("You are in the elevator.")


def print_menu():
    return ("""
Please enter the number for the floor you would like to visit:
1. Lobby
2. HR
3. Engineering
4. Exit
\n""")


def validate_input(prompt, options):
    while True:
        input_response = input(prompt).lower()

        for option in options:
            if option in input_response:
                return option

        print_pause("Sorry, I don't understand.")


def first_floor():
    print_pause("You pushed the button for the first floor.")
    print_pause("After a few moments you find yourself in the lobby.")
    if "Id Card" in items:
        print_pause("The clerk greets you, but she has already given you your id card, so nothing more to do here.")
    else:
        print_pause("The clerk greets you and gives you your id card.")
        items.append("Id Card")


def second_floor():
    print_pause("You pushed the button for the second floor.")
    print_pause("After a few moments you find yourself in HR.")

    if "Handbook" not in items:
        print_pause("The head of HR greets you.")

        if "Id Card" not in items:
            print_pause("You must get your Id card, before I can give you a handbook.")
        else:
            print_pause("He looks at your ID card and then gives you a copy of the employee handbook.")
            items.append("Handbook")
    else:
        print_pause("HR is busy.  Nothing to do here.")

    print_pause("You head back to the elevator.")


def third_floor():
    print_pause("You pushed the button for the third floor.")
    print_pause("After a few moments you find yourself in engineering.")
    print_pause("You use your ID card to open the door.")

    if "Id Card" not in items:
        print_pause("Unfortunately, the door is locked.  'Maybe I need a card key?'")
    else:
        print_pause("Your manager greets you and tells you that you need a copy of the handbook to start work.")
        if "Handbook" not in items:
            print_pause("Your manager instructs you to go to HR and get a handbook.")
        else:
            print_pause("Congratulations!  You start work!")

    print_pause("You head back to the elevator.")


def get_user_selection():
    while True:
        choice = validate_input(print_menu(), ["1", "2", "3", "4"])
        if choice == "1":
            first_floor()
        elif choice == "2":
            second_floor()
        elif choice == "3":
            third_floor()
        else:
            break


def ride_elevator():
    # items = []
    intro()
    get_user_selection()
    print_pause("Good-bye!")


ride_elevator()

