#!/usr/bin/python3

def InQueue(list1,data):
    list1.append(data)
def DeQueue(list1):
    return list1.pop(0)
def isFull(list1):
    return  len(list1) == 10
def isEmpty(list1):
    return  list1 == None or list1 == []

def queue_using_list():
    list1=[]
    while True:
        print("\n1.InQueue the element:")
        print("2.DeQueue the element:")
        print("3.Display:")
        print("4.Exit")
        ch = eval(input("Enter the choice:"))
        if ch < 1 or ch > 4:
            print("Invalid input, Please try again.")
            continue    
        if ch == 1:
            if not isFull(list1):
                data=eval(input("Enter the data:"))
                InQueue(list1,data)
    
        elif ch == 2:
            if not isEmpty(list1):
                print("Dequeue element is {}".format(DeQueue(list1)))
        elif ch == 3:
            print("Queue is {}".format(list1))
        elif ch == 4:
            print("Good bye")
            break


if __name__ == "__main__":
     queue_using_list()



