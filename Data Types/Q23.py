# Python program to check a list is empty or not.


def list_check(my_list):
        if len(my_list) == 0:
            print("List is empty")
        else:
            print("List is not empty")


list_check([])
list_check([1, 2, 3])
