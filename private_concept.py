#!/usr/bin/python3
""" This example is for private member and private method"""

class A():
    __var=10
    def __ini__(self):
        pass
    def __fun(devi):
        print("Inside fun.")
obj = A()
print("Class namespace:\n{}".format(dir(A)), end="\n\n")
print("Object Namespace:\n{}".format(dir(obj)), end="\n\n")

print(obj._A__var)
print(A._A__var)
obj._A__fun()
A._A__fun(A())

#We can not access private variable and method directly because name-mangling happen when name start with __ and not end with __ 

#print(obj.__var)
#print(obj.__fun())
