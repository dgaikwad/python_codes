#!/usr/bin/python3

""" Program to sort list using insertion sort algorithm. 

For good understanding purpose watch video by geekforgeek using below link
https://www.youtube.com/watch?v=OGzPmgsI-pQ

"""
def insertion_sort(list1):
    if list1 == None:
        return True
    for index in range(1, len(list1)):
        current_value = list1[index]
        position = index
        while position > 0 and list1[position - 1] > current_value:
            list1[position] = list1[position-1]
            position = position -1
        list1[position] = current_value

def main():
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("Before list:", a_list)
    insertion_sort(a_list)
    print("After list :", a_list)

if __name__ == "__main__":
    main()


