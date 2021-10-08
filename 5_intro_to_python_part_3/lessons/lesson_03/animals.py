class Dog:
    # class vars
    scientific_name = "Canis lupus familiaris"

    def __init__(self, name):
        self.name = name
        self.count = 0

    def bark_count(self):
        self.count += 1
        for val in range(self.count):
            self.speak()

    def speak(self):
        print("Bowow!")

    def eat(self, food):
        if food == "biscuit":
            print("Yummy!")
        else:
            print("That's not food!")

    def hear(self, words):
        if self.name in words:
            self.speak()


class Husky(Dog):
    origin = "Siberia"

    def speak(self):
        print("Husky Woof!")


class Chihuahua(Dog):
    origin = "Mexico"

    def speak(self):
        print("Chihuahua yip!")


class Labrador(Dog):
    origin = "Canada"

    def speak(self):
        print("Labrador bark!")


class Cat:
    def __init__(self):
        self.mood = "neutral"

    def speak(self):
        if self.mood == "happy":
            print("Purr")
        elif self.mood == "angry":
            print("Hiss!")
        else:
            print("Meow!")


if __name__ == '__main__':
    fido = Dog("Fido")
    # fido.speak()
    # print(fido.name)
    # fido.hear("fido.  where are you?")
    # fido.name2 = "fido 2"
    # print(fido.name2)

    fido.bark_count()
    fido.bark_count()
    fido.bark_count()

    snow_dog = Husky("Snow")
    print(snow_dog.origin)
    snow_dog.speak()
    print()
    snow_dog.bark_count()
    print()
    snow_dog.bark_count()
    print()
    snow_dog.bark_count()
