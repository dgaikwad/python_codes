#!/usr/bin/python3

""" Binary search program """

def binary_search(list1, data):
    first=0
    last = len(size) - 1 
    while first <= last:
        mid = (first + last) // 2
        if data == list1[mid]:
            return mid
        elif data > list1[mid]:
             first = mid + 1
        else:
            last = mid - 1
    return False

if __name__ == "__main__"    :
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]    
    print(binary_search(testlist, 3))
    print(binary_search(testlist, 32))

