#!/usr/bin/python3


def merge_two_sorted_list(first, second):
    """ Program to merge two sorted list into third list"""

    if not first:
        return second
    elif not second:
        return first
    result=[]
    counter=0
    len1 = len(first)
    len2 = len(second)

    lenght = len1 if len1 <= len2 else len2
    i = j = 0
    while True:
        if len(first) == i:
            return result + second[j:]

        if len(second) == j:
            return result + first[i:]

        if first[i] <= second[j]:
            result.append(first[i])
            i +=1
        else:
            result.append(second[j])
            j += 1

if __name__ == "__main__":
    list1 = ["a","c", "d", "h", "k" ]
    list2 = ["b", "e", "f"]
    list3 = merge_two_sorted_list(list1, list2)
    print("First input list {}".format(list1))
    print("Second input list {}".format(list2))
    print("Output list {}".format(list3))
