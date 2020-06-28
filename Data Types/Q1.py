# count the number of characters in a string.


def char_count(str1):
    result = {}
    for i in str1:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result


print(char_count('google.com'))

