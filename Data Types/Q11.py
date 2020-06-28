# Python program to count the occurrences of each word in a given
# sentence.

string = input("enter a sentence: ")
result = {}
for word in string.split(' '):
    if word in result:
        result[word] += 1
    else:
        result[word] = 1
print(result)

