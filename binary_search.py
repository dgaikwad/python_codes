#!/usr/bin/python3

""" Binary search tree program """

def binary_search(list1, data):
    size = len(list1)
    found = False
    first=0
    last=size - 1 
    mid= size // 2
    while first <= last and not found:
        mid = (first + last) // 2
        if data == list1[mid]:
            found = True
        else:
            if data > list1[mid]:
                first = mid + 1
            else:
                last=mid - 1
    return found    
if __name__ == "__main__"    :
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]    
    print(binary_search(testlist, 3))
    print(binary_search(testlist, 32))

