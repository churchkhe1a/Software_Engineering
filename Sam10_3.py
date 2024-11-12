def sum_with_two(number):

  try:
    result = 2 + int(number)
    print(f"Результат сложения: {result}")
  except ValueError:
    print("Неподходящий тип данных. Ожидалось число.")

if __name__ == '__main__':
  print("Тест 1: Ввод числа")
  sum_with_two(5) # Ввод числа

  print("\nТест 2: Ввод строки")
  sum_with_two("hello") # Ввод строки

  print("\nТест 3: Ввод некорректного числа")
  sum_with_two("12.5") # Ввод некорректного числа
