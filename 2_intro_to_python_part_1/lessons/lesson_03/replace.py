# Add your code here:
def replace_substring(string, target, replacement):
    output = []
    len_target = len(target)
    index = 0

    while index < len(string):
        if string[index:index + len_target] == target:
            # target found, replace it
            output.append(replacement)
            index += len_target
        else:
            output.append(string[index])
            index += 1

    return "".join(output)


# Here are some examples you can test it with:
print(replace_substring('Hot SPAM!drop soup, and curry with SPAM!plant.', 'SPAM!', 'egg'))
print(replace_substring("The word 'definately' is definately often misspelled.", 'definately', 'definitely'))

