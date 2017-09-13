#!/usr/bin/python3

""" Program to sort list using bubble sort algorithm. """

def bubble_sort(list1):
    size = len(list1)
    flag = True
    for pass1 in range(size-1,0,-1):
        if flag == False:
            break
        else:   
             pass
        flag = False
        for inner in range(pass1):
            if list1[inner] > list1[inner+1]:
                list1[inner],list1[inner+1]=list1[inner+1],list1[inner]
                flag = True
def main():
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("Before: ",a_list)
    bubble_sort(a_list)
    print("After : ",a_list)
if __name__ == "__main__":
    main()

            
            


