#!/usr/bin/python3
""" Program to count substring from string.

Example:
    input string : "abaaabasecababascgaba"
    pattern : "abc"
    output : 5
"""

def count_pattern(input_str, pattern):
    count = 0
    for i in range(len(input_str) - (len(pattern) -1)):
        if input_str[i:i+len(pattern)] == pattern:
            count += 1
    return count


if __name__ == "__main__":
    input_str = "abaaabasecababascgaba"
    pattern = "aba"
    result = count_pattern(input_str, pattern)
    print("{} is fount in {} {}  times.".format(pattern, input_str, result))

   
 
