def repeat():
    response = input("Can you guess what my favorite color is?\n")
    if response == 'blue':
        print("That's right! My favorite color is blue.")
    else:
        print("Sorry, that's not my favorite color. Try again!")
        repeat()


repeat()

