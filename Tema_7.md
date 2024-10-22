# Тема 7.  Работа с файлами (ввод, вывод)
Отчет по Теме #7 выполнил(а):
- Обласова Александра Владимировна
- ИВТ-22-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + | - |
| Задание 7 | + | - |
| Задание 8 | + | - |
| Задание 9 | + | - |
| Задание 10 | + | - |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк. 

```python
Sometimes I think
But then I forget
```

### Результат.
![image](https://github.com/user-attachments/assets/2618f385-82ee-490b-8128-d8b72a90aa81)

## Вывод
Создан тектовый файл для дальнейшей работы.

## Лабораторная работа №2
### Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().

```python
f = open('input.txt', 'r')
print(f.readline())
f.close()
```

### Результат.
![image](https://github.com/user-attachments/assets/0a42c512-02ab-4555-bba0-88e05400d9ee)

## Вывод
1. `open('input.txt', 'r')` открывает файл `"input.txt"` для чтения.
2. `f.readline()` считывает первую строку из файла.
3. `print()` выводит прочитанную строку на экран.
4. `f.close()` закрывает файл, освобождая ресурсы.


## Лабораторная работа №3
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().

```python
f = open('text.txt', 'r')
print(f.readlines())
f.close()
```

### Результат.
![image](https://github.com/user-attachments/assets/9bedef2b-fe64-45ab-b8be-df97cf831fe2)

## Вывод
1. Программа открывает файл `text.txt` в режиме чтения (`'r'`).
2. Использует `readlines()` для чтения всех строк в список и выводит этот список.
3. Закрывает файл с помощью `f.close()`.
  
## Лабораторная работа №4
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().

```python
with open('text.txt') as f:
    print(f.readlines())
```

### Результат.
![image](https://github.com/user-attachments/assets/59783d6b-8111-4094-bb0e-614811f289f0)

## Вывод
1. Программа открывает файл `text.txt` в режиме чтения (`'r'`) с помощью `with` блока.
2. Использует `readlines()` для чтения всех строк в список и выводит этот список.
3. `with` автоматически закрывает файл после завершения блока.

## Лабораторная работа №5
### Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().

```python
with open('text.txt') as f:
    for line in f:
        print(line)
```

### Результат.
![image](https://github.com/user-attachments/assets/71b9b924-3084-4455-9e15-f1919638af0c)

## Вывод
1. Программа открывает файл `text.txt` в режиме чтения (`'r'`) с помощью `with` блока.
2. Использует цикл for для итерации по каждой строке файла и выводит ее на консоль.
3. `with` автоматически закрывает файл после завершения блока.

## Лабораторная работа №6
### Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.

```python
with open('text.txt', 'a+') as f:
    f.write('\nIm small and stupid')

with open('text.txt', 'r') as f:
    result = f.readlines()
    print(result)
```

### Результат.
![image](https://github.com/user-attachments/assets/48ea25e6-9e87-4941-a9a4-4917655117f4)
![image](https://github.com/user-attachments/assets/a5993e35-e614-4af1-80b4-75bb133203ae)

## Вывод
1. Программа открывает файл `text.txt` в режиме добавления и чтения (`'a+'`).
2. Использует `write()` для добавления новой строки в конец файла.
3. Открывает файл в режиме чтения (`'r'`) и выводит его содержимое.

## Лабораторная работа №7
### Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить что измененная вами информация сохранилась в файле.

```python
lines = ['one', 'two', 'three']
with open ('text.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done!')
```

### Результат.
![image](https://github.com/user-attachments/assets/a6081e38-bda3-4644-9f5e-e6397a78d267)
![image](https://github.com/user-attachments/assets/f4bdbf76-36c9-41bb-a8c6-05cd9a833fed)

## Вывод
1. Программа создает список `lines` со строками.
2. Открывает файл `text.txt` в режиме записи (`'w'`) с помощью `with` блока.
3. В цикле `for` записывает в файл каждую строку из `lines` с добавлением префикса.
4. `with` автоматически закрывает файл после завершения блока.

## Лабораторная работа №8
### Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).

```python
import os

def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка{catalog[0]} содержит:')
    print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
    print(f'Файлы: {", ".join([file for file in catalog[2]])}')
    print('-' * 40)


print_docs(r'C:\Users\Aleks\Software_Engineering\pic')
```

### Результат.
![image](https://github.com/user-attachments/assets/b041820e-8047-45e2-9102-d170f5e8cd23)

## Вывод
1. Программа импортирует модуль `os` для работы с файловой системой.
2. Определяет функцию `print_docs`, которая принимает на вход путь к директории.
3. Использует `os.walk` для итерации по всем файлам и папкам в указанной директории.
4. Выводит на консоль информацию о каждой папке и ее содержимом (файлах и подпапках).

## Лабораторная работа №9
### Документ «input.txt» содержит следующий текст:
### Приветствие
### Спасибо
### Извините
### Пожалуйста
### До свидания
### Ты готов?
### Как дела?
### С днем рождения!
### Удача!
### Я тебя люблю.
### Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько). Проверьте работоспособность программы на своем наборе данных

```python
def longest_words(file):
    with open (file, encoding='utf-8') as f:
        words = f.read().split()
        max_length = len(max(words, key=len))
        for word in words:
            if len(word) == max_length:
                sought_words = word

        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words


print(longest_words('text.txt'))
```

### Результат.
![image](https://github.com/user-attachments/assets/8b4c3066-4cc1-4f98-8e31-bfed45d3550a)

## Вывод
1. Программа импортирует модуль `os` для работы с файловой системой.
2. Определяет функцию `longest_words`, которая принимает на вход путь к файлу.
3. Открывает файл в режиме чтения (`'r'`) с помощью `with` блока.
4. Использует `read().split()` для получения списка всех слов из файла.
5. Находит максимальную длину слова в списке.
6. Итерация по всем словам из списка и сохранение всех слов с максимальной длиной в `sought_words`.
7. Возвращает найденные слова.

## Лабораторная работа №10
### Требуется создать csv-файл «rows_300.csv» со следующими столбцами: 
### • № - номер по порядку (от 1 до 300);
### • Секунда – текущая секунда на вашем ПК; 
### • Микросекунда – текущая миллисекунда на часах. 
### Для наглядности на каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.


```python
import csv
import datetime
import time

with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда ', 'Микросекунда'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second,
                         datetime.datetime.now().microsecond])
        time.sleep(0.01)
```

### Результат.
![image](https://github.com/user-attachments/assets/f0b0df23-d5fc-405a-befd-5f4fdb95df02)
![image](https://github.com/user-attachments/assets/03deadca-c778-45f2-86ee-beea085f994b)

## Вывод
1. Программа импортирует модули `csv`, `datetime` и `time`.
2. Открывает файл `rows_300.csv` в режиме записи (`'w'`) с помощью `with` блока.
3. Создает объект `csv.writer` для записи данных в файл.
4. Записывает заголовок таблицы.
5. В цикле `for` записывает в файл строки с текущей секундой, микросекундой и номером строки.
6. Использует `time.sleep` для задержки между записями.

## Самостоятельная работа №1
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.

```python
from collections import Counter
import re


def analyze_text_file(directory):
    try:
        with open(directory, 'r', encoding='utf-8') as file:
            text = file.read()
        words = re.findall(r'\b\w+\b', text.lower())
        word_count = len(words)
        word_frequency = Counter(words)
        most_common_word, most_common_count = word_frequency.most_common(1)[0]
        print(f"Количество слов в файле: {word_count}")
        print(f"Самое часто встречающееся слово: '{most_common_word}' (встречается {most_common_count} раз)")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
analyze_text_file(r'C:\Users\Aleks\PycharmProjects\Tema7\bananacat.txt')
```

### Результат.
![image](https://github.com/user-attachments/assets/528c1fad-cfbb-49ec-9d1b-ea832361496e)

## Вывод
1. Импортирует модуль `Counter` из `collections` для подсчета частоты слов и модуль re для регулярных выражений.
2. Определяет функцию `analyze_text_file`, которая принимает путь к файлу в качестве аргумента.
3. Открывает файл в режиме чтения с кодировкой `utf-8м и использует `with open(...)` для автоматического закрытия файла.
4. Применяет регулярные выражения для извлечения слов из текста с помощью `re.findall(r'\b\w+\b', text.lower())`.
5. Вычисляет общее количество слов и определяет частоту каждого слова с помощью `Counter(words)м.
6. Выводит общее количество слов и самое часто встречающееся слово с его частотой.
7. Использует `try-except` для обработки исключений, которые могут возникнуть при открытии или чтении файла.
8. Вызывает функцию `analyze_text_file` с указанным путем к файлу.
  
## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.

```python
def record_expense(filename):
    while True:
        expense_item = input("Введите название расхода (или 'отмена' для выхода): ")
        if expense_item.lower() == 'отмена':
            break
        expense_amount = input("Введите данные расходов:")

        with open(filename, 'a', encoding='utf-8') as file:
            file.write(f"{expense_item}: {expense_amount}\n")

    print()
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())

filename = 'text.txt'
record_expense(filename)
```

### Результат.
![image](https://github.com/user-attachments/assets/4cf1069f-8312-454e-ae17-149209181292)
![image](https://github.com/user-attachments/assets/a354c549-bbc9-422b-9388-511385a15535)

## Вывод
1. Определяет функцию `record_expense`, которая принимает имя файла в качестве аргумента.
2. Использует цикл `while True` для получения ввода пользователя о названии расхода и сумме.
3. Открывает файл в режиме добавления (`'a'`) и записывает в него полученные данные.
4. После завершения ввода, открывает файл в режиме чтения (`'r'`) и выводит его содержимое.
5. Использует `with open(...)` для автоматического закрытия файла.
6. Вызывает функцию `record_expense` с указанным именем файла.

## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу,которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.
### • Текст в файле:
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
### • Ожидаемый результат:
Input file contains:
108 letters
20 words
4 lines

```python
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
```

### Результат.
![image](https://github.com/user-attachments/assets/542dbcde-8f5a-4a6a-835c-844f6041cc54)

## Вывод
1. Определяет функцию `analyze_text`, которая принимает путь к файлу в качестве аргумента.
2. Открывает файл в режиме чтения и считывает все строки в список с помощью `readlines()`.
3. Использует цикл `for` для подсчета букв, слов и строк в файле.
4. Выводит информацию о количестве букв, слов и строк в файле.
5. Использует `with open(...)` для автоматического закрытия файла.
6. Вызывает функцию `analyze_text` с указанным путем к файлу.

## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.
### • Запрещенные слова: hello email python the exam wor is
### • Предложение для проверки: Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!
### • Ожидаемый результат: *****, ***ld! ****** ** *** programming language of *** future. My ***** **.... ****** ** awesome!!!!

```python
import re

def load_banned_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]
def replace_banned_words(sentence, banned_words):
    for word in banned_words:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        sentence = pattern.sub('*' * len(word), sentence)
    return sentence
def main():
    banned_words = load_banned_words('text.txt')
    sentence = "Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!"
    result = replace_banned_words(sentence, banned_words)
    print("Результат:", result)
if __name__ == "__main__":
    main()
```

### Результат.
![image](https://github.com/user-attachments/assets/2a6a46b2-2a51-4a40-9df9-bf90c61f778e)

## Вывод
1. Определение функций:  
    - Определяет функцию `load_banned_words`, которая читает список запрещенных слов из файла.
    - Определяет функцию `replace_banned_words`, которая заменяет запрещенные слова в тексте на звездочки.
    - Определяет функцию `main`, которая управляет основной логикой программы.
2. Вызывает функцию `load_banned_words` для загрузки списка запрещенных слов из файла.
3. Применяет функцию `replace_banned_words` для замены запрещенных слов в тексте.
4. Выводит результат замены.
5. Использует `with open(...)` для автоматического закрытия файла.
6. Вызывает функцию `main` для запуска программы.

## Самостоятельная работа №5
### Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.
### Представьте, что у вас есть текстовый файл с произвольным текстом. Вам необходимо написать программу, которая проанализирует этот файл и определит 10 самых часто встречающихся слов в тексте. 

```python
from collections import Counter

def top_10_words(file_path):

  with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read().lower()
    words = text.split()
    word_counts = Counter(words)
    top_10 = word_counts.most_common(10)
    return top_10

file_path = 'text.txt'
top_words = top_10_words(file_path)

print("10 самых частых слов:")
for word, count in top_words:
  print(f"{word}: {count}")
```

### Результат.
![image](https://github.com/user-attachments/assets/4edb0bde-6cfc-440d-b33c-a15fa015a8cc)

## Вывод
1. Импортирует модуль `Counter` из `collections` для подсчета частоты слов.
2. Определяет функцию `top_10_words`, которая принимает путь к файлу в качестве аргумента.
3. Открывает файл в режиме чтения и считывает текст.
4. Преобразует текст в нижний регистр, разделяет его на слова и подсчитывает частоту каждого слова с помощью `Counter(words)`.
5. Выводит 10 самых частых слов с их частотой.
6. Использует `with open(...)` для автоматического закрытия файла.
7. Вызывает функцию `top_10_words` с указанным путем к файлу.

## Общие выводы по теме

