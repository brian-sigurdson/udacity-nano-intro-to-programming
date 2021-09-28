import os


def locate_delimiters(string, target):
    found_at = []

    if target in string:
        num_targets = string.count(target)
        if num_targets != 2:
            return -1
        else:
            first_target_index = string.find(target)
            string = string[first_target_index + 1:]
            second_target_index = string.find(target)
            # print(string)
            # print(second_target_index)
            found_at.append(first_target_index)
            found_at.append(first_target_index + 1 + second_target_index)
            return found_at
    else:
        return -1


def extract_place(string, delimiter):
    delimiter_positions = locate_delimiters(string, delimiter)
    # print(string)
    # print(delimiter_positions)
    # move the starting position + 1 to skip the first delimiter
    return string[delimiter_positions[0] + 1: delimiter_positions[1]]


photo_files = os.listdir("Photos")
places = []

for file_name in photo_files:
    place = extract_place(file_name, "_")
    places.append(place)

print(places)
