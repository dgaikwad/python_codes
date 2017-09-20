#!/usr/bin/python3
""" Program to sort list using selection sort """

def selection_sort(list1):
    size = len(list1)

    if size == None:
        return list1

    for index in range(size):
        min_index = index
        for n_index in range(index+1, size):
            if list1[n_index] < list1[min_index]:
                min_index = n_index
        list1[index],list1[min_index] = list1[min_index],list1[index] 

    return list1

def main():
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("Before list:", a_list)
    selection_sort(a_list)
    print("After list :", a_list)

if __name__ == "__main__":
    main()


