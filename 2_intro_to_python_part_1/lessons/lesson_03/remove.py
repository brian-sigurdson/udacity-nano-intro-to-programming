# Add your code here:
def remove_substring(string, target):
    output = []
    len_target = len(target)
    index = 0

    while index < len(string):
        if string[index:index + len_target] == target:
            # target found, skip it
            index += len_target
        else:
            output.append(string[index])
            index += 1

    return "".join(output)


# Here are some strings you can test your function:
print(remove_substring('SPAM!HelloSPAM! worldSPAM!!', 'SPAM!'))
print(remove_substring("Whoever<br> wrote this<br> loves break<br> tags!", "<br>"))
print(remove_substring('I am NOT learning to code.', 'NOT '))

