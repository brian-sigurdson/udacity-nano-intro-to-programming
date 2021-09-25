def locate_all(string, target):
    found_at = []
    index = 0
    while index < len(string):
        if string[index : index + len(target)] == target:
            found_at.append(index)
        index += 1

    if len(found_at) == 0:
        return -1
    else:
        return found_at


# Here are a couple function calls to test with.
# This one should return 1
print(locate_all('cookbook', 'ook'))

# This one should return -1
print(locate_all('all your bass are belong to us', 'base'))

print(locate_all('yesyesyes', 'yes'))