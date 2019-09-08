def fibonacci_series(n):

  num1 = 0
  num2 = 1
  num3 = 0

  if n < 1:
    print(f"Number {n} should be greater than 0")
    return False
  for _ in range(0, n):    
    num1 = num2
    num2 = num3
    print(num3, end="\t")
    num3 = num1+num2
    
  print()
fibonacci_series(0)
fibonacci_series(1)
fibonacci_series(10)


