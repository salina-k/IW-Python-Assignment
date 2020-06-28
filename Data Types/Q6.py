# Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.


def replace_substring(str1):
    keyword1 = str1.find('not')
    keyword2 = str1.find('poor')
    if 'not' in str1:
        if keyword2 > keyword1:
            str1 = str1. replace(str1[keyword1:(keyword2+4)], 'good')
    else:
        return str1

    return str1


print(replace_substring('The lyrics is not that poor!'))
print(replace_substring('The lyrics is poor!'))



