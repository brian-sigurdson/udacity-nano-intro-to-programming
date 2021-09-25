s = "This is a sentence. This is another."


def until_dot(val):
    tmp = ""
    index = 0
    while index < len(val) and val[index] != '.':
        index += 1

    return val[:index]


print(until_dot(s))
