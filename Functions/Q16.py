# Python program to square and cube every number in a given list of
# integers using Lambda.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list: ", my_list)
sqr = list(map(lambda x: x ** 2, my_list))
print("list of square : ", sqr)
cube = list(map(lambda x: x ** 3, my_list))
print("list of square : ", cube)
