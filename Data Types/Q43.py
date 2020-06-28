# Python program to remove an item from a tuple

t1 = (1, 2, 3, 4, 5)
n = int(input("enter index of the item to remove: "))
new_tuple = t1[:n] + t1[n+1:]
print(new_tuple)
