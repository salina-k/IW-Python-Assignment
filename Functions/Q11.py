# Python program to create a lambda function that adds 15 to a given
# number passed in as an argument, also create a lambda function that multiplies
# argument x with argument y and print the result.

# lambda function that adds 15 to a number given by user

def add(y):
    return lambda x: x + y


n = int(input("Enter a number: "))
number1 = add(n)
print("Sum of the input number with 15 is: ", number1(15))



# lambda function that multiplies two numner given by user

def multi(y):
    return lambda x: x * y


n1 = int(input("Enter a number to multiply: "))
number1 = multi(n1)
n2 = int(input("Enter a number to multiply: "))
print("The product is: ", number1(n2))
