# Python program to remove the nth index character from a non-empty string.


def remove_nth_char():
    string = input("enter a string: ")
    n = int(input("enter the index to remove: "))
    first = string[:n]
    last = string[n+1:]
    print(first + last)


remove_nth_char()

