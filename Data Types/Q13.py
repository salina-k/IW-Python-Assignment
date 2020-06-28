# Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically).


string = input("enter comma separated sequence of words: ").split(",")
string = sorted(string)
print("Sorted: " + ','.join(string))


# my_string = input("enter words here: ")
# result = [x.strip() for x in my_string.split(',')]
# print ("Sorted: " + ','.join(sorted(result)))

