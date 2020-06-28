# Python program to reverse a string.


def reverse(string):
    result = string[::-1]
    return result


n = input("Enter a string: ")
print(reverse(n))
