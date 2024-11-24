# Тема 11. Итераторы и генераторы.
Отчет по Теме #11 выполнил(а):
- Обласова Александра Владимировна
- ИВТ-22-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | - | - |
| Задание 7 | - | - |
| Задание 8 | - | - |
| Задание 9 | - | - |
| Задание 10 | - | - |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Простой итератор, но у него нет гибкой настройки, например его нельзя развернуть. Он работает просто как next(), но нет prev().

```python
numbers = [0,1,2,3,4,5]
for item in numbers:
    print(item)
```

### Результат.
![image](https://github.com/user-attachments/assets/7cceed4a-55c8-4cba-b671-4ae46b012a0e)



## Вывод
1. `slots = ['name']`: Этот атрибут класса `slots` указывает Python, что в классе `Sasha` можно использовать только атрибут `name`.
2. `init(self, name)`: Конструктор класса. Он принимает имя человека как аргумент и сравнивает его со своим именем. 
3. `person2.surname = 'Обласова'` - попытка присвоить `person2` атрибут `surname`. Эта строка вызовет ошибку `AttributeError: 'Sasha' object has no attribute 'surname'`, поскольку `Sasha` не определяет атрибут `surname`.

## Лабораторная работа №2
### Класс итератор с гибкой настройкой и удобными применением.

```python
class CountDown:
    def __init__(self, start):
        self.count = start + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.count -=1
        if self.count < 0:
            raise StopIteration
        return self.count

if __name__== "__main__":
    counter = CountDown(5)
    for i in counter:
        print(i)
```

### Результат.
![image](https://github.com/user-attachments/assets/ecd8531c-ec8b-4d02-8168-a991c29fb08f)



## Вывод
1. `__init__(self, ingredient=None)`: Конструктор класса. Он принимает опциональный аргумент `ingredient`.
2. `isinstance(ingredient, str)`: Проверяет, является ли `ingredient` строкой. Если да, то присваивает значение `ingredient` атрибуту `self.ingredient`.
3. `self.ingredient = None`: Если `ingredient` не строка, то присваивает `None` атрибуту `self.ingredient`.
4. `composition(self)`: Метод для вывода состава мороженого.
5. `if self.ingredient:`: Проверяет, есть ли значение в `self.ingredient`.

## Лабораторная работа №3
### Генератор списка.

```python
a = [i**2 for i in range(1,5)]

print('a-', a)
for i in a:
    print(i)

print('iter(a) -', iter(a))
for i in a:
    print(i)
```

### Результат.
![image](https://github.com/user-attachments/assets/5e899c68-9fe5-411e-8712-9c36a265a9b5)



## Вывод
Ошибка `AttributeError: 'MyClass' object has no attribute 'value'` возникает, потому что в коде происходит обращение к несуществующему атрибуту `value`. После того как был вызван `del_value()`, атрибут `value` был удален, но в коде происходит попытка его вывода.

## Лабораторная работа №4
### Выражения генераторы.

```python
b = (i**2 for i in range(1,5))
print(b)
print('first')
for i in b:
    print(i)
print('second')

for i in b:
    print(i)
```

### Результат.
![image](https://github.com/user-attachments/assets/e600d036-6780-4cc5-867e-c007d1fd7186)


## Вывод
1. `className = 'Mammal'`: Устанавливает атрибут `className` для класса `Mammal`.
2. `species = 'canine'`: Добавляет атрибут для определения вида животного.
3. `sounds = 'wow'`: Добавляет атрибут для звуков, которые издает животное.
4. `species = 'feline'`: Добавляет атрибут для определения вида животного.
5. `sounds = 'meow'`: Добавляет атрибут для звуков, которые издает животное.

## Лабораторная работа №5
### Такой же счетчик, как и в первом задании, только это генератор и использует yield.

```python
def countdown(count):
    while count>=0:
        yield count
        count -=1

if __name__== '__main__':
    counter = countdown(5)
    for i in counter:
        print(i)
```

### Результат.
![image](https://github.com/user-attachments/assets/ace15914-4a94-4d4e-a98a-1b831311470f)



## Вывод
1. `@staticmethod`: Декоратор, который обозначает, что метод является статическим. Статические методы не требуют создания экземпляра класса для вызова.
2. `greeting()`: Метод, который выводит приветствие на соответствующем языке.
3. Функция `greet(language)`: Принимает объект класса `Russian` или `English` как аргумент и вызывает метод `greeting()` у переданного объекта, чтобы получить приветствие на соответствующем языке.

## Самостоятельная работа №1
### Вас никак не могут оставить числа Фибоначчи, очень уж они вас заинтересовали. Изучив новые возможности Python вы решили реализовать программу, которая считает числа Фибоначчи припомощи итераторов. Расчет начинается с чисел 1 и 1. Создайте функцию fib(n), генерирующую n чисел Фибоначчи с минимальными затратами ресурсов. Для реализации этой функции потребуется обратиться к инструкции yield (Она не сохраняет воперативной памяти огромную последовательность, а дает возможность “доставать” промежуточные результаты по одному).Результатом решения задачи будет листинг кода и вывод в консоль с числом Фибоначчи от 200.

```python
def fib(n):
  a, b = 1, 1
  for _ in range(n):
    yield a
    a, b = b, a + b

fib_sequence = fib(200)

for i in range(199):
  next(fib_sequence)
print(f"200-е число Фибоначчи: {next(fib_sequence)}")
```

### Результат.
![image](https://github.com/user-attachments/assets/3081137e-135e-4600-a40b-2dc1c7b72748)



## Вывод
1. `slots = ['name']`: Этот атрибут класса `slots` указывает Python, что в классе `Sasha` можно использовать только атрибут `name`.
2. `init(self, name)`: Конструктор класса. Он принимает имя человека как аргумент и сравнивает его со своим именем. 
3. `person2.surname = 'Обласова'` - попытка присвоить `person2` атрибут `surname`. Эта строка вызовет ошибку `AttributeError: 'Sasha' object has no attribute 'surname'`, поскольку `Sasha` не определяет атрибут `surname`.

## Самостоятельная работа №2
### К коду предыдущей задачи добавьте запоминание каждого числа Фибоначчи в файл “fib.txt”, при этом каждое число должно находиться на отдельной строчке. Результатом выполнения задачи будет листинг кода и скриншот получившегося файла

```python
def fib(n):
  a, b = 1, 1
  for _ in range(n):
    yield a
    a, b = b, a + b

fib_sequence = fib(200)

with open("fib.txt", "w") as f:
  for i in range(200):
    num = next(fib_sequence)
    f.write(str(num) + "\n")

print(f"200-е число Фибоначчи: {num}")
```

### Результат.
![image](https://github.com/user-attachments/assets/af2637a6-df8d-425d-b475-b4d9ca9a78cb)

![image](https://github.com/user-attachments/assets/eadf343c-aa50-4a78-bde0-391083e97641)
