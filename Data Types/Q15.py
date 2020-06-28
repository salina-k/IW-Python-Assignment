# Python function to insert a string in the middle of a string.


def insert_string_middle(bracket, string):
    result = bracket[0:2] + string + bracket[2:]
    return result


print(insert_string_middle('[[]]', 'Python'))
print(insert_string_middle('{{}}', 'PHP'))
