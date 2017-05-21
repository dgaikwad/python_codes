#!/usr/bin/python3

class Stack:
    def __init__(self):
        self.l1=[]
        self.size=10

    def Push(self, data):
        if not self.IsFull():
            self.l1.append(data)
        else:
            print("Stack is Full")

    def IsEmpty(self):
        if len(self.l1) == 0:
            return True

    def IsFull(self):
        if len(self.l1) == 10:
            return True
            
    def Pop(self):
        if not self.IsEmpty():
            return self.l1.pop()
        else:
            print("Stack is Empty, we can't pop element")

    def Display(self):
        print("\nStack contains Following elements:")
        for i in self.l1:
            print(i,end="\t")

class Queue:
    def __init__(devi):
        devi.l1 = []

    def Push(devi, data):
        devi.l1.append(data)

    def Pop(devi):
        return devi.l1.pop()

    def Display(devi):
        print("\nQueue contains Following elements:")
        for data in devi.l1:
            print(data, end="\t")
        print()
                
def QueueOpr():
    q1 = Queue()
    q1.Push(11)
    q1.Push(12)    
    q1.Push(13) 
    q1.Display()
    print("\nRemoved elements from Queue is : {}".format(q1.l1.pop(0)))    
    q1.Display()

def StackOpr():
    s1=Stack()
    s1.Push(10)
    s1.Push(20)
    s1.Push(30)
    s1.Display()
    print("\nPoped elements from Stack is : {}".format(s1.Pop()))
    s1.Display()

def main():
    StackOpr()
    QueueOpr()

if __name__ == "__main__":
    main()







