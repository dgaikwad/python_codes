#!/usr/bin/python3
from collections import Counter
"""
Program is checking the each character count from given string.
"""
def count_occurence(check_string):
    count = {}
    for s in check_string:
      if s in count.keys():
        count[s] += 1
      else:
        count[s] = 1
    print("Below are the character and occurences:")
    for key in count:
      if count[key] > 1:
        print(key, "=", count[key])

# Below function is second solution for same problem statement

def count_occurence_2(check_string):
    count1 = Counter()
    for char in check_string:
        count1[char] += 1
    print("Below are the character and occurences:")  
    for key in count1:
        print(key,"=", count1[key])

if __name__ == "__main__":
    input_str = "Program is checking the each character count from given string"
    count_occurence(input_str)
    count_occurence_2(input_str)


