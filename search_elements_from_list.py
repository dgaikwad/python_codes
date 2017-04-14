#!/usr/bin/python3

def serch_ele(input_list,element):
    for i in input_list:
        if i == element:
            return True
    return False



if __name__ == "__main__":
    input_list=list(eval(input("Enter list elements comma separated:")))
    element = eval(input("Enter the elements which you wants search:"))
    result = serch_ele(input_list,element)
    if result == True:
        print("Element {0} is found in list".format(element))
    else:
        print("Element {0} is not found in list".format(element))

