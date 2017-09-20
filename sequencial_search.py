#!/usr/bin/python3

""" Sequencial search  program """

"""
Complexity:
Best case = 1
Average = n/2
Worst case = n
"""

def sequencial_search(list1, data):

    found = False
    for index in range(len(list1)):
        if list1[index] == data:
            found = True
            break
    return found
    
if __name__ == "__main__"    :
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]    
    print(sequencial_search(testlist, 3))
    print(sequencial_search(testlist, 32))

