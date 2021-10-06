dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# print keys
for key in dictionary:
    print(key)

# print keys
for key in dictionary.keys():
    print(key)

# print values
for value in dictionary.values():
    print(value)

# print (key, value) tuples
for item in dictionary.items():
    print(item)

for item in dictionary.items():
    print(f"item[0] = {item[0]}")
    print(f"item[1] = {item[1]}")

# print the contents of each tuple
for key, value in dictionary.items():
    print(f"key = {key}; value = {value}")


d = {"color": "purple", "number": 42, "animal": "turtle", "language": "python"}

for key, value in d.items():
    print(f"my favorite {key} is {value}")

