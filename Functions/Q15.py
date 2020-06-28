# Python program to filter a list of integers using Lambda.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list: ", my_list)
even_num = list(filter(lambda x: x % 2 == 0, my_list))
print("list of even no. : ", even_num)
odd_num = list(filter(lambda x: x % 2 != 0, my_list))
print("list of odd no. : ", odd_num)
