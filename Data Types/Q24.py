# Python program to clone or copy a list.


def clone_list(li1):
    li1_copy = li1.copy()
    return li1_copy


li1 = [1, 2, 3]
li2 = clone_list(li1)
print("List1 is: ", li1)
print("Clone of list1 is: ", li2)
