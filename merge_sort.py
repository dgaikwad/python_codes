#!/usr/bin/python3


"https://www.youtube.com/watch?v=EeQ8pwjQxTM"

def merge_sort(list1):
    print("Splitting: ", list1)
    if len(list1) > 1:
        mid = len(list1) // 2
        left = list1[0:mid]
        right = list1[mid:]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        while i < len(left) and j<len(right) :
            if left[i] < right[j]:
                list1[k] = left[i]
                i = i+1
            else:
                list1[k] = right[j] 
                j = j+1

            k = k+1
        while i < len(left):
            list1[k]=left[i]
            k=k+1
            i=i+1
        while j< len(right):
            list1[k] = right[j]
            j=j+1
            k=k+1   


list1 = [54,26,93,17,77,31,44,55,20]
merge_sort(list1)
print(list1)



























        
