sentence = "it appears that the the appears the most in the sentence"

split_it = sentence.split(" ")

word_count = {}

for value in split_it:
    word_count[value] = sentence.count(value)

for key, value in word_count.items():
    print(f"key = {key}; value = {value}")
