numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

value = int(input("Введите значение переменной: "))

if value in numbers:
  print(f"Переменная {value} есть в массиве")
  if value % 2 == 0:
    print(f"Переменная {value} четная")
  else:
    print(f"Переменная {value} нечетная")
else:
  print(f"Переменной {value} нет в массиве")
