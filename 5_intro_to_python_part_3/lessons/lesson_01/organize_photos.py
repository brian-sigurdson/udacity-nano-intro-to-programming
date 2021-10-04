import os
import shutil


os.chdir("Photos")
originals = os.listdir()
places = []


def make_place_directories(the_places):
    # places_set = set(the_places)

    for val in the_places:
        os.mkdir(val)


def extract_place(string, delimiter):
    # the filename will look something like "2021-03-04_<place>_other-stuff"
    # This splits the string and returns the second element, which will
    # contain the place call "<place>"
    return string.split(delimiter)[1]


def clean_up(the_places):
    places_set = set(the_places)

    # for each sub-directory created to hold files for a particular place
    for place in places_set:
        # get the filenames in the folder
        filenames = os.listdir(place)
        # for each filename
        for filename in filenames:
            # move it to the parent directory
            os.rename(filename, os.path.join("../", filename))

        # now remove the sub-directories
        shutil.rmtree(place)



def extract_filenames():
    for filename in originals:
        place = extract_place(filename, "_")
        if place not in places:
            places.append(place)


def move_files():
    for filename in originals:
        place = extract_place(filename, "_")
        os.rename(filename, os.path.join(place, filename))


extract_filenames()
make_place_directories(places)
print(places)
print(os.listdir())
move_files()


input("Hit any key to cleanup.\n")
clean_up(places)


