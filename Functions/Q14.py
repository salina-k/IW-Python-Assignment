# Python program to sort a list of dictionaries using Lambda.

my_dict = [{'num': 10}, {'num': 5}, {'num': 15}, {'num': 12}]
sorted_dict = sorted(my_dict, key=lambda x: x['num'])
print("Sorting the List of dictionaries :")
print(sorted_dict)
