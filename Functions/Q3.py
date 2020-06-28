# Python function to multiply all the numbers in a list.


def sum_num(my_list):
    mul = 1
    for i in my_list:
        mul = mul * i
    return mul


print(sum_num((8, 2, 3, 0, 7)))
print(sum_num((8, 2, 3, -1, 7)))

