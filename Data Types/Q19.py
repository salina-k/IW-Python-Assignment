# Python program to get the largest number from a list.


def largest(my_list):
    result = min(my_list)
    return result


print(largest([1, 4, -5, 7, 10]))
print(largest([0, 4, 59, 77, 1]))
