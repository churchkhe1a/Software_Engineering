class DataError(Exception): # Исключение, которое возникает при ошибке обработки данных
  pass


def calculate_average(numbers): # Вычисляет среднее арифметическое чисел в списке

  for number in numbers:
    if not isinstance(number, (int, float)):
      raise DataError("Список должен содержать только числа.")
  return sum(numbers) / len(numbers)


def process_data(data): # Обрабатывает данные, проверяя на корректность

  if not isinstance(data, str):
    raise DataError("Данные должны быть строкой.")
  if not data.isdigit():
    raise DataError("Данные должны содержать только цифры.")
  print(f"Обработанные данные: {data}")


if __name__ == '__main__':
  try:
    average = calculate_average([1, 2, 'a', 4]) # Некорректный ввод в список
  except DataError as e:
    print(f"Ошибка: {e}")

  print("\nОбработка данных:")
  try:
    process_data("123abc") # Некорректные данные
  except DataError as e:
    print(f"Ошибка: {e}")

  try:
    process_data("456") # Корректные данные
  except DataError as e:
    print(f"Ошибка: {e}")
