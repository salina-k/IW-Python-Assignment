# Python program that multiplies all the items in a list.


def multiply_list_items(list_item):
    result = 1
    for i in list_item:
        result = i * result
    return result


print(multiply_list_items([1, 2, 3]))
print(multiply_list_items([10, 20, 30]))
