numbers = [1, 2, 3, 4, 5]

number = int(input("Введите значение переменной: "))

if number in numbers:
  print(f"Переменная {number} есть в массиве")
else:
  print(f"Переменной {number} нет в массиве")
