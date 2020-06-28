# Python function to create the HTML string with tags around the
# word(s).


def add_tags(tag, string):
    result = '<' + tag + '>' + string + '</' + tag + '>'
    return result


print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))
