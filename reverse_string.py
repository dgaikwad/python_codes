
# Print the reverse string of the original string

def reverseSTR(str1):
    if type(str1) != str:
        raise TypeError(f"{str1} type should be string not {type(str1)}")
      
    str_len = len(str1) - 1
    while str_len >= 0:
        print(str1[str_len], end="")
        str_len -= 1

    
    print()
    
    str_len = len(str1)
    for index in range(str_len-1, -1 , -1):
        print(str1[index], end="")
        

reverseSTR("Hello")
reverseSTR("")
#reverseSTR(2323) # should get error here
