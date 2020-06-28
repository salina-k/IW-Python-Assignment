# Python program to check whether all dictionaries in a list are empty or
# not.


def dict_check(my_list):
    for dict in my_list:
        if dict:
            return False
        else:
            return True


print(dict_check([{}, {}, {}]))
print(dict_check([{1, 2}, {}, {}]))

