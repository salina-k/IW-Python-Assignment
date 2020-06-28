# Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument.


def calculate_factorial(num):
    if num != 0:
        result = 1
        for i in range(1, num+1):
            result = result * i
        return result


n = int(input("Enter a non-negative number: "))
print(calculate_factorial(n))
