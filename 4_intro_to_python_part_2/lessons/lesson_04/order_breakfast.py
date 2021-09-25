# vars
stop = False


# methods
def order_again():
    while True:
        another_order = input("Do you want another order? (yes or no)\n")
        if "yes" in another_order.lower() or "y" in another_order.lower():
            return True
        elif "no" in another_order.lower() or "n" in another_order.lower():
            return False
        else:
            print("Sorry.  I didn't understand that response.")


while not stop:
    response = input("Please place your order.  Would you like waffles or pancakes?\n")

    if "waffles" in response.lower():
        print("Waffles it is!")
        if order_again():
            continue
        else:
            break

    elif "pancakes" in response.lower():
        print("Pancakes it is!")
        if order_again():
            continue
        else:
            break
    else:
        print("Sorry.  I don't understand that response.")
