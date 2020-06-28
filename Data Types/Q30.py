# Python script to check whether a given key already exists in a
# dictionary.


def check_key(dict1):
    key = input("enter the key to check: ")
    if key in dict1:
        return "key already exists in the dictionary"
    else:
        return "key does not exist in the dictionary"


print(check_key({'0': 10, '1': 20, '2': 30}))
