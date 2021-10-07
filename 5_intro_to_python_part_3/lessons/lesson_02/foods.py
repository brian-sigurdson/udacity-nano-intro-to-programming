foods = [['apple', 'banana', 'orange'], ['carrot', 'cucumber', 'tomato']]

# Here's a basic loop that gives one of the above results.
# Give it a try, and then modify it to see what other
# results you can get.
# for e in foods:
#     print(e)

# loop 1
for item in foods:
    print(item)

# loop 2
for item in foods[0]:
    print(item)

# loop 3
for item in foods:
    print(item[0])

