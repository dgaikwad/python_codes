#!/usr/bin/python3




def factorial(number):
    if number == 0:
        return 1
    if  number >= 1:
        total=number*factorial(number-1)
    return total
if __name__ == "__main__":
    total=1
    value=eval(input("Enter the value for find gactorial="))
    if value >= 0:
        print("Factorial is {}".format(factorial(value)))
    else:
        print("Factorial does not support for negative value, Pleas enter range between 0...n")
    
