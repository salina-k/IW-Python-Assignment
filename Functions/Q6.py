# Python function to check whether a number is in a given range.


def check_range(num):
    lr = int(input("enter lower range: "))
    hr = int(input("enter higher range: "))
    if num in range(lr, hr):
        print("Yes, %s  is in the range" % str(num))
    else:
        print("No, %s is not in the range" % str(num))


n = int(input("enter a number: "))
check_range(n)
