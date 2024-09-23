string = "Привет, мир!"
value = input()

found = False

for i in string:
  if i == value:
    found = True
    print(f"Символ '{value}' найден в строке")
    # index = string.find(value)
    # print(f"Индекс символа: {index}")
    break

else:
  print(f"Символа '{value}' нет в строке")
