# Python program to sort a list of tuples using Lambda.


def tuple_sort(tup):
    tup.sort(key=lambda x: x[1])
    return tup


tup = [('python', 20), ('hello', 5), ('world', 10)]
print(tuple_sort(tup))
