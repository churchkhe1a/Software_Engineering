class EmptyFileException(Exception):
  pass

def read_file(filename):

  with open(filename, 'r', encoding='utf-8') as file:
    data = file.read()
    if not data.strip():
      raise EmptyFileException("Файл пустой")
    print(data)

if __name__ == '__main__':
  try:
    read_file('empty_file.txt') # Пустой файл
  except EmptyFileException as e:
    print(f"Ошибка: {e}")

  try:
    read_file('data_file.txt') # Файл с данными
  except EmptyFileException as e:
    print(f"Ошибка: {e}")
