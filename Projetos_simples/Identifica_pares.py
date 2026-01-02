def is_even(number):
  return number % 2 == 0  
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Números pares:")
for num in numbers:
  if is_even(num):
    print(num)
