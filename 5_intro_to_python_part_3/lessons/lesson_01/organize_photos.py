import os
import shutil


originals = os.listdir("Photos")
places = []


def make_place_directories(the_places):
    # places_set = set(the_places)

    for val in the_places:
        os.mkdir(f"Photos/{val}")


def extract_place(string, delimiter):
    # the filename will look something like "2021-03-04_<place>_other-stuff"
    # This splits the string and returns the second element, which will
    # contain the place call "<place>"
    return string.split(delimiter)[1]


def clean_up(the_places):
    places_set = set(the_places)

    for val in places_set:
        shutil.rmtree(f"Photos/{val}")


def extract_create_move():
    for file_name in originals:
        place = extract_place(file_name, "_")
        if place not in places:
            places.append(place)


extract_create_move()
make_place_directories(places)
print(places)
print(os.listdir("Photos"))


input("Hit any key to cleanup.\n")
clean_up(places)


