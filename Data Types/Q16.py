# Python program to sum all the items in a list.


def sum_items(list_item):
    result = sum(list_item)
    return result


print(sum_items([1, 2, 3, 4, 5]))
print(sum_items([10, 20, 30, 40, 50]))
print(sum_items([1, 2, -8]))
