# Python program to add 'ing' at the end of a given string (length should
# be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
# string length of the given string is less than 3, leave it unchanged.

str1 = input("enter a string: ")
if len(str1) >= 3:
    for i in str1:
        if 'ing' in str1:
            result = str1 + 'ly'
        else:
            result = str1 + 'ing'
    print(result)

else:
    print(str1)
