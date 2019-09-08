def reverse_number(num):
  if num < 0:
    print("Please enter positive number.")
    return False
  result  = 0 
  while num != 0:

    reminder  =  num % 10 
    result = result *10 + reminder
    num = num // 10
    
  return result

for no in [-1, 0, 213, 1234]:
  output = reverse_number(no)
  print(output)
