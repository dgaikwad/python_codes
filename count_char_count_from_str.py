#!/usr/bin/python3
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
        print(key, count[key])


if __name__ == "__main__":
    input_str = "i am checking this string to see how many times each character appears"
    count_occurence(input_str)








