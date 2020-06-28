# Python function that takes a list of words and returns the length of the
# longest one.

words_list = ['Hello', 'Hello world', 'world']
longest = 0
for word in words_list:
    if len(word) > longest:
            longest = len(word)
print(longest)









