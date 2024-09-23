numbers = [2, 4, 6, 8, 10]
flag = False

for number in numbers:
  if number % 2 != 0:
    flag = True
    break

if flag is True:
  print("В массиве есть нечетное число")
else:
  print("В массиве нет нечетных чисел")
