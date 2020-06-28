# Python function that accepts a string and calculate the number of
# upper case letters and lower case letters.


def upper_lower(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.islower():
            lower_count += 1

        elif char.isupper():
            upper_count += 1
        
    print("No. of Upper case characters : ", upper_count)
    print("No. of Lower case characters : ", lower_count)


n = input("enter a string: ")
upper_lower(n)

