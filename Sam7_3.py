def analyze_text(directory):
  with open(directory, 'r', encoding='utf-8') as file:
    lines = file.readlines()

  total_letters = 0
  total_words = 0
  total_lines = len(lines)

  for line in lines:
    total_letters += sum(1 for c in line if c.isalpha())
    total_words += len(line.split())

  print("Input file contains:")
  print(f"{total_letters} letters")
  print(f"{total_words} words")
  print(f"{total_lines} lines")

analyze_text(r'C:\Users\Aleks\PycharmProjects\Tema7\text.txt')
