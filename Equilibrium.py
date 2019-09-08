"""Find Equilibrium index of an array. Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.
Ex: Input: arr[] = {-7, 1, 5, 2, -4, 3, 0}

      Output: 3

      3 is an equilibrium index, because: arr[0] + arr[1] + arr[2] = arr[4] + arr[5] + arr[6]"""

def Equilibrium(input_list):
    length = len(input_list)

    if not length >= 2:
        return -1
    left_sum = []
    sum  = 0
    for index in range(length):
        left_sum.append(sum)

        sum = sum + input_list[index]

    sum = 0
    right_sum = [0 for i in range(length)]  
    for index in range(length-1, 0, -1):
        right_sum[index] = sum
        sum = sum + input_list[index]

    for i in range(1, length-1):
        if left_sum[i] == right_sum[i]:
            return i
    else:
        return -1

       
   
       
result  = Equilibrium([-7, 1, 5, 2, -4, 3, 0])    
print(result)
