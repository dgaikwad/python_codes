#!/usr/bin/python3

from collections import Counter;
dict1 = Counter ();
file_name = input("Enter file name to count each word occurences:")
fd = open(file_name, "r")
lines = fd.readlines() 
for line in lines:
    for word in line.split ():
        dict1 [word] += 1
for word in dict1:
    print(word,"=", dict1[word])
