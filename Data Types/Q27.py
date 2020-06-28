# Python program to replace the last element in a list with another list.


def replace_last(list1, list2):
    list1 = list1[: -1] + list2
    return list1


print(replace_last([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]))
print(replace_last([1, 3, 5, 7, 9, 10, 100, 200], [2, 4, 6, 8]))
