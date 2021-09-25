# Write your code here
def is_substring(substring, string):
    substring_len = len(substring)
    string_len = len(string)

    if substring_len > string_len:
        return False

    for val in range(string_len - substring_len):
        # print(string[val: val + substring_len])
        if string[val: val + substring_len] == substring:
            return True

    return False


# Below are some calls you can use to test it
# This one should return False
print(is_substring('bad', 'abracadabra'))

# This one should return True
print(is_substring('dab', 'abracadabra'))