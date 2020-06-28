# Python function that takes a list and returns a new list with unique
# elements off of the first list.


def remove_duplicate(list1):
    my_list = []
    for items in list1:
        if items not in my_list:
            my_list.append(items)
    return my_list


print(remove_duplicate([1, 2, 3, 3, 3, 3, 4, 5]))
