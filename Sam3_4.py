sentence = input("Введите предложение: ")
print("Длина предложения:", len(sentence))
print("В нижнем регистре:", sentence.lower())

vowels = "aeiou"
vowel_count = 0
for char in sentence:
  if char in vowels:
    vowel_count += 1
print("Количество гласных:", vowel_count)

replaced_sentence = sentence.replace("ugly", "beauty")
print("Замена 'ugly' на 'beauty':", replaced_sentence)

if sentence.startswith("The ") or sentence.startswith("the "):
  print("Предложение начинается с 'The'")
else:
  print("Предложение не начинается с 'The'")

if sentence.endswith(" end"):
  print("Предложение заканчивается на 'end'")
else:
  print("Предложение не заканчивается на 'end'")
