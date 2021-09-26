import time


def print_pause(string):
    print(string)
    time.sleep(0)


def intro():
    print_pause("Hello! I am Bob, the Breakfast Bot.")
    print_pause("Today we have two breakfasts available.")
    print_pause("The first is waffles with strawberries and whipped cream.")
    print_pause("The second is sweet potato pancakes with butter and syrup.")


def validate_input(prompt, options):
    while True:
        input_response = input(prompt).lower()

        for option in options:
            if option in input_response:
                return option

        print_pause("Sorry, I don't understand.")


def order_again():
    while True:
        another_order = validate_input("Do you want another order? (yes or no)\n", ["yes", "y", "no", "n"]).lower()
        if "yes" in another_order or "y" in another_order:
            get_order()
        elif "no" in another_order or "n" in another_order:
            return
        else:
            print_pause("Sorry.  I didn't understand that response.")


def get_order():
    response = validate_input(
        """Please place your order. Would you like waffles or pancakes?\n""",
        ["waffles", "pancakes"]
    ).lower()

    if "waffles" in response:
        print_pause("Waffles it is!")
    elif "pancakes" in response:
        print_pause("Pancakes it is!")
    else:
        print_pause("Sorry.  I don't understand that response.")

    print_pause("Your order will be ready shortly.")


def order_breakfast():
    intro()
    get_order()
    order_again()
    print_pause("Okay.  Good-bye.")


order_breakfast()
