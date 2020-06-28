# Python program to print the even numbers from a given list.


def even_number(list1):
    my_list = []
    for i in list1:
        if i % 2 == 0:
            my_list.append(i)
    print(my_list)


even_number([1, 2, 3, 4, 5, 6, 7, 8, 9])
