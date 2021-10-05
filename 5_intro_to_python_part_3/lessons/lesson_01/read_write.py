with open("output.txt", "w") as output:
    for val in range(31):
        if val % 2 == 0:
            output.write(f"{val}\n")


with open("read.txt") as reader:
    with open("copy.txt", "w") as copy:
        copy.write(reader.read())

