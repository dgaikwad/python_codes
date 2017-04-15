#!/usr/bin/python3
def sum_list(list1):
    sum=0
    count=len(list1)
    for i in range(1,count+1):
        print(i)
        sum=sum+i
    print("Sum of all list elememts={0}".format(sum))


if __name__ == "__main__":
    list_input=list(eval(input("Enter the comma separated.")) )
    sum_list(list_input)





