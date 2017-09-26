#!/usr/bin/python3
"""
    Merger the two sorted list into first list.

"""


def merge_list(list1, list2):
    list1.extend(list2)
    list1=sorted(list1)
    return list1

if __name__ == "__main__":
    list1 = [1,2,4]
    list2 = [3,5,6]
    print("Input list \nlist1:{}\nlist2:{}".format(list1, list2))
    print("Output list is : ", merge_list(list1, list2))

