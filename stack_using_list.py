#!/usr/bin/python3

def Push(list1,data):
    list1.append(data)
def Pop(list1):
    return list1.pop()
def isFull(list1):
    return  len(list1) == 10
def isEmpty(list1):
    return  list1 == None or list1 == []

def stack_using_list():
    list1=[]
    while True:
        print("1.Push the element:")
        print("2.Pop the element:")
        print("3.Display:")
        print("4.Exit")
        ch = eval(input("Enter the choice:"))
        if ch < 1 or ch > 4:
            print("Invalid input, Please try again.")
            continue    
        if ch == 1:
            if not isFull(list1):
                data=eval(input("Enter the data:"))
                Push(list1,data)
        elif ch == 2:
            if not isEmpty(list1):
                print(Pop(list1))
        elif ch == 3:
            print(list1)
        elif ch == 4:
            print("Good bye")
            break


if __name__ == "__main__":
     stack_using_list()



