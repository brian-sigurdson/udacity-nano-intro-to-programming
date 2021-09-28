import os


def extract_place(string, delimiter):
    # the filename will look something like "2021-03-04_<place>_other-stuff"
    # This splits the string and returns the second element, which will
    # contain the place call "<place>"
    return string.split(delimiter)[1]


photo_files = os.listdir("Photos")
places = []

for file_name in photo_files:
    place = extract_place(file_name, "_")
    places.append(place)

print(places)
