#!/usr/bin/python3
""" Program to sort list using selection sort """

def selection_sort(list1):
    size = len(list1)
    if size == None:
        return list1
    for i in range(size):
        min = i
        for j in range(i+1, size):
            if list1[j] < list1[min]:
                min = j
        list1[i],list1[min] = list1[min],list1[i] 
    return list1

def main():
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("Before list:", a_list)
    selection_sort(a_list)
    print("After list :", a_list)

if __name__ == "__main__":
    main()


