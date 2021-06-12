#fizz buz game
for number in range(1, 101):
  if number % 3==0 and number % 5 ==0:
    print("FIZBUZZ")
  elif number % 5 == 0:
    print("BUZZ")
  elif number % 3 != 0:
    print(number)
  elif number % 3==0:
    print("FIZZ")
