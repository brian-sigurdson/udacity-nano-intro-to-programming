# Add your code here.
def total_length(string_lists):
    count = 0
    for a_string in string_lists:
        if a_string is not None:
            count += len(a_string)

    return count


# Should return 6:
print(total_length(['foo', 'bar']))

# Should return 0 (it's an empty list):
print(total_length([]))

# Should return 8:
print(total_length(['balloons']))

# Should return 0 (it has four empty strings):
print(total_length(["", '', "", '']))

print(total_length([]))

