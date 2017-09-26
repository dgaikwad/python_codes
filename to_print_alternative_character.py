#!/usr/bin/python3

def alternative_char(filename, char):
    """ To print the alternative character to specific size """
    with open(filename, "rb") as fd:
        line = fd.read(char)
        fd.seek(0,0)
        while len(line) > 0 and line != "" and line != "b''":
            line = fd.read(char)
            print(str(line,"utf-8"))
            fd.seek(char,1)
            line = fd.read(char)

if __name__ ==  "__main__":
    file_name = (input("Enter the file name :"))
    char_size = eval(input("Enter how much character want to print alternate: "))
    alternative_char(file_name, char_size)

