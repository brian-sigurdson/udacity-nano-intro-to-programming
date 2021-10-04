import os
import shutil


def make_place_directories(places):
    places = set(places)

    for val in places:
        os.mkdir(val)


def extract_place(string, delimiter):
    # the filename will look something like "2021-03-04_<place>_other-stuff"
    # This splits the string and returns the second element, which will
    # contain the place call "<place>"
    return string.split(delimiter)[1]


def extract_filenames(originals, places):
    for filename in originals:
        place = extract_place(filename, "_")
        if place not in places:
            places.append(place)


def move_files(originals):
    for filename in originals:
        place = extract_place(filename, "_")
        os.rename(filename, os.path.join(place, filename))


def organize_photos(directory):
    os.chdir(directory)
    originals = os.listdir()
    places = []

    extract_filenames(originals, places)
    make_place_directories(places)
    print(places)
    print(os.listdir())
    move_files(originals)


# organize_photos("Photos")
print("TEST")


