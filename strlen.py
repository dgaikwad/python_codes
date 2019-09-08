def strlen(str1):
    count = 0
    if type(str1) != str:
        raise TypeError(f"{str1} type should be string not {type(str1)}")
        
    for char in str1:
        count += 1
    print(count)

strlen("Hello")
strlen("")
#strlen(232)
