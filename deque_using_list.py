#!/usr/bin/python3
def InsertLast(list1,data):
    list1.append(data)
def InsertFirst(list1,data):
    list1.insert(0,data)    

def DeleteFirst(list1):
    return list1.pop(0)

def DeleteLast(list1):
    len1=len(list1)
    return list1.pop(len1-1)
def First(list1):
    if list1 != None or list1 != []:
        return list1[0]
    else:
        print("List is empty")
def Last(list1):
    if list1 != None or list1 != []:    
        len1=len(list1)
        return list1[len1-1]
    else:
        print("List is empty")
    
def isFull(list1):
    return  len(list1) == 10

def isEmpty(list1):
    return  list1 == None or list1 == []

def Deque_using_list():
    list1=[]
    while True:
        print("\n1.Insert element at first posotion.")
        print("2.Insert at element at last position.")
        print("3.Delete element at first position.")
        print("4.Delete element at last position.")
        print("5.show first elemet.")
        print("6.Show last element.")
        print("7.Display:")
        print("8.Exit")
        ch = eval(input("Enter the choice:"))
        if ch < 1 or ch > 8:
            print("Invalid input, Please try again.")
            continue    
        if ch == 1:
            if not isFull(list1):
                data=eval(input("Enter the data:"))
                InsertFirst(list1,data)
        elif ch == 2:
            if not isFull(list1):
                data=eval(input("Enter the data:"))
                InsertLast(list1,data)               
        elif ch == 3:
            if not isEmpty(list1):
                print("Deleted value from first is {}".format(DeleteFirst(list1)))
        elif ch == 4:
            if not isEmpty(list1):
                print("Deleted value from last  is {}".format(DeleteLast(list1)))
        elif ch == 5:
            print("First element is {}".format(First(list1)))
        elif ch == 6:
            print("Last element is {}".format(Last(list1)))
        elif ch == 7:
              print("Queue is {}".format(list1))
        elif ch == 8:
            print("Good bye")
            break

if __name__ == "__main__":
     Deque_using_list()



