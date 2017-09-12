#!/usr/bin/python3

#Linked list class contains only one variable is head which hold the link list and class providing basic funtionality

class LinkedList():
    def __init__(self):
        self.head=None

    def is_empty(self):
        return True if self.head == None else False

    def insert_first(self, data):
        tmp = Node(data)
        tmp.next = self.head
        self.head=tmp

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.get_next()
        print("Linked list contains {} elements.".format(count)) 
        return count
    def search(self, data):
        count = 0
        current = self.head
        while current != None:
            if current.get_data() ==  data:
                print("{0} fount in linked list".format(data))
                break
            else:
                current = current.get_next()
        else:
            print("{0} not fount in linked list".format(data))


    def remove(self, data):
        current = self.head
        previouse = None
        found = False
        while current != None and not found:
            if  current.data == data:
                found = True
            else:
                previouse = current
                current = current.get_next()
        if not found:
            print("Element not found.")
            return False                 
        if previouse == None:
            self.head = current.get_next()
            
        else:
            previouse.next = (current.get_next())
            del current
    def remove_first(self):
        if self.head != None:
            current = self.head
            self.head = current.next
            del current
    def remove_last(self):
        if self.head != None:
            current = self.head
            previouse = None
            while current.next != None:
                previouse = current
                current = current.next
            del current
            previouse.next = None


    def display(self):
        if self.head == None:
            return
        current = self.head
        while current != None:
            print("{} ".format(current.data), end="\t")
            current = current.get_next()
        print()
    def insert_last(self, data):
        current = self.head
        while current.next != None:
            current = current.next
        tmp = Node(data)
        current.next = tmp
        
    def insert_specific_position(self, data, pos):
        size = self.size()        
        if pos > (size + 1) or pos < 1:
            print("Invalid position.")
            return False
        if pos == size+1:
            self.insert_last(data)
            return True
        if pos == 1:
            self.insert_first(data)
            return True
        current = self.head
        prev = None
        counter = 1
        while counter < pos-1:
            current = current.next
            counter += 1
        tmp = Node(data)
        tmp.next = current.next
        current.next = tmp
        return True

    def remove_specific_position(self, pos):
        size = self.size()
        if pos < 1 or pos > size:
            print("Invalid position")
            return False
        if pos == 1:
            self.remove_first()
            return True
        if pos == size:
            self.remove_last()
            return True
        current = self.head
        prev = None
        counter = 1
        while counter < pos-1:
            current = current.next
            counter += 1
        tmp = current.next
        current.next = current.next.next
        del tmp
        return True

        

#class Node is actual class which contains the data and next data variable which is holding address of next node

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
    def get_data(self):
        return self.data
    def set_data(self,next_data):
        self.data=next_data
    def get_next(self):
        return self.next
    def set_next(self, new_next):
        self.next = new_next

def main():
    operation = True
    mobj = LinkedList()
    while operation:
        print("*"*100,"\nCurrent linked list contains is below:")
        mobj.display()    
        print("*"*100)
        print("\n1.Display linked list")
        print("2.Insert at first")
        print("3.Remove at first")  
        print("4.Insert at last")
        print("5.Remove last")
        print("6.Search Element")
        print("7.Insert at specific position")
        print("8.Remove from specific position")
        print("9.Count linked list size")
        print("10.Remove specific element") 
        print()


        input1 = eval(input("Your choice:"))
        if input1 == 1:
            mobj.display()
        elif input1 == 2:
            data = eval(input("Enter the data:"))
            mobj.insert_first(data)
        elif input1 == 3:
            mobj.remove_first()
        elif input1 == 4:
            data = eval(input("Enter the data:"))
            mobj.insert_last(data)
        elif input1 == 5:
            mobj.remove_last()
        elif input1 == 6:
            data = eval(input("Enter the element to search:"))
            mobj.search(data)
        elif input1 == 7:
            data,pos = eval(input("Enter the data and position commama separator for insertion:"))
            mobj.insert_specific_position(data, pos)
        elif input1 == 8:
            pos = eval(input("Enter position for remove data :"))
            mobj.remove_specific_position(pos)
        elif input1 == 9:
            mobj.size()
        elif input1 == 10:
            data = eval(input("Enter the element which want to remove:"))
            mobj.remove(data)
                    
        operation=input("Do you want to perform more operation y/n : ")    
        operation = True if "y" == operation else False



if __name__ ==  "__main__":
    main()

