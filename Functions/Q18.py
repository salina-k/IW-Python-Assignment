# Python program to check whether a given string is number or not
# using Lambda.

num = lambda x: True if x.isnumeric() else False

print(num('python'))
print(num('379'))
print(num('000'))
