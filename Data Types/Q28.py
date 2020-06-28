# Python script to add a key to a dictionary.


def add_key():
    my_dict = {0: 10, 1: 20}
    my_dict.update({2: 30})
    return my_dict


print(add_key())
