#!/usr/bin/python3
def count_special_ch(string):
    count=0
    for i in string:
        if (i.isupper() or i.islower() or i.isdigit()) == True:
            pass
        else:
            count +=1
    return count
if __name__=="__main__":
    inputstr=input("Enter the string to count special character=")
    count=count_special_ch(inputstr)	
    print("Special character Count is {0}".format(count))    	
