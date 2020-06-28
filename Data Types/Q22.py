# Python program to remove duplicates from a list.


def remove_duplicates(my_list):
    result = []
    for i in my_list:
        if i not in result:
            result.append(i)
    return result


list1 = [1, 2, 3, 4, 2, 1, 10, 15, 4, 10]

print(remove_duplicates(list1))
