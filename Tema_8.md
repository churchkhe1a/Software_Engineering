# Тема 8. Введение в ООП
Отчет по Теме #8 выполнил(а):
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
### Создайте класс “Car” с атрибутами производитель и модель. Создайте объект этого класса. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями.

```python
class Car: # определение класса Car
  def __init__(self, make, model): # метод инициализации класса (конструктор)
    self.make = make # создание атрибута make и присваивание ему значения аргумента make
    self.model = model # создание атрибута model и присваивание ему значения аргумента model

my_car = Car("Toyota", "Corolla") # создание объекта класса Car с именем my_car,
                  # передавая в конструктор значения "Toyota" и "Corolla" для атрибутов make и model
```

### Результат.
![image](https://github.com/user-attachments/assets/4ed5bc7d-b0b3-4bf8-93a1-c5bde69be9e3)

## Вывод
1. `def __init__(self, make, model):`: Определяет специальный метод `__init__`, который является конструктором класса. Он вызывается автоматически при создании нового объекта этого класса.
2. `self` - ссылка на создаваемый объект.
3. `make` и `model` - параметры, которые будут использоваться для инициализации атрибутов.
4. `self.make = make`: Создается атрибут make объекта класса `Car` и ему присваивается значение параметра `make`.
5. `self.model = model`: Создается атрибут model объекта класса `Car` и ему присваивается значение параметра `model`.
6. `my_car = Car("Toyota", "Corolla")`: Создается объект класса `Car` с именем `my_car`. При создании объекта в конструктор передаются значения "Toyota" и "Corolla" для атрибутов `make` и `model`.
Этот код демонстрирует создание класса в Python. Класс - это blueprint для создания объектов с определенными атрибутами (характеристиками). В этом случае мы создали класс для представления автомобиля с атрибутами "марка" и "модель".

## Лабораторная работа №2
### Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину “поехать”. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car: # определение класса Car
  def __init__(self, make, model): # метод инициализации класса (конструктор)
    self.make = make # создание атрибута make и присваивание ему значения аргумента make
    self.model = model # создание атрибута model и присваивание ему значения аргумента model

  def drive(self): # метод класса для имитации вождения
    print(f"Driving the {self.make} {self.model}") # вывод сообщения о вождении автомобиля

my_car = Car("Toyota", "Corolla") # создание объекта класса Car с именем my_car,
                 # передавая в конструктор значения "Toyota" и "Corolla" для атрибутов make и model
my_car.drive() # вызов метода drive() для объекта my_car
```

### Результат.
![image](https://github.com/user-attachments/assets/5597b10d-a2f1-4b3b-8808-4713cdce1e92)

## Вывод
1. Добавлен метод `drive()`, который имитирует действие "езда" и выводит сообщение.
2. Вызов метода `drive()` для объекта `my_car` заставляет машину "поехать".
Код демонстрирует работу класса с методом, который имитирует действие.

## Лабораторная работа №3
### Создайте новый класс “ElectricCar” с методом “charge” и атрибутом емкость батареи. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом заряжаться. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car: # определение класса Car (базовый класс)
  def __init__(self, make, model): # метод инициализации класса (конструктор)
    self.make = make # создание атрибута make и присваивание ему значения аргумента make
    self.model = model # создание атрибута model и присваивание ему значения аргумента model

  def drive(self): # метод класса для имитации вождения
    print(f"Driving the {self.make} {self.model}") # вывод сообщения о вождении автомобиля

my_car = Car("Toyota", "Corolla") # создание объекта класса Car с именем my_car,
                 # передавая в конструктор значения "Toyota" и "Corolla" для атрибутов make и model
my_car.drive() # вызов метода drive() для объекта my_car

class ElectricCar(Car): # определение класса ElectricCar, наследующего от класса Car
  def __init__(self, make, model, battery_capacity): # метод инициализации класса ElectricCar
    super().__init__(make, model) # вызов конструктора родительского класса Car для инициализации атрибутов make и model
    self.battery_capacity = battery_capacity # создание атрибута battery_capacity и присваивание ему значения аргумента battery_capacity

  def charge(self): # метод класса для имитации зарядки
    print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh") # вывод сообщения о зарядке автомобиля

my_electric_car = ElectricCar("Tesla", "Model S", 75) # создание объекта класса ElectricCar с именем my_electric_car,
                          # передавая в конструктор значения "Tesla", "Model S" и 75 для атрибутов make, model и battery_capacity
my_electric_car.drive() # вызов метода drive() (наследованного от класса Car) для объекта my_electric_car
my_electric_car.charge() # вызов метода charge() для объекта my_electric_car
```

### Результат.
![image](https://github.com/user-attachments/assets/9a007b96-9f0a-4379-b177-dbb08848bc37)

## Вывод
Этот код демонстрирует как можно использовать наследование для создания новых классов, расширяющих функциональность существующих классов. Он также демонстрирует как методы могут вести себя по-разному в разных классах (полиморфизм).

## Лабораторная работа №4
### Реализуйте инкапсуляцию для класса, созданного в первом задании. Создайте защищенный атрибут производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car: # определение класса Car
  def __init__(self, make, model): # метод инициализации класса (конструктор)
    self._make = make # создание атрибута _make (защищенного) и присваивание ему значения аргумента make
    self.__model = model # создание атрибута __model (частного) и присваивание ему значения аргумента model

  def drive(self): # метод класса для имитации вождения
    print(f"Driving the {self._make} {self.__model}") # вывод сообщения о вождении автомобиля

my_car = Car("Toyota", "Corolla") # создание объекта класса Car с именем my_car,
                 # передавая в конструктор значения "Toyota" и "Corolla" для атрибутов _make и __model
print(my_car._make) # вывод значения атрибута _make объекта my_car (доступен извне класса)
my_car.drive() # вызов метода drive() для объекта my_car
```

### Результат.
![image](https://github.com/user-attachments/assets/0b96094d-f599-4256-b56d-2b19746f7f67)

## Вывод
1. `my_car = Car("Toyota", "Corolla")`: Создает объект класса `Car` с именем `my_car`, передавая значения "Toyota" и "Corolla".
2. `my_car.drive()`: Вызывает метод `drive()`, который выводит сообщение о вождении автомобиля.
Код демонстрирует, как реализовать инкапсуляцию в Python, используя соглашения о наименовании для создания защищенных и приватных атрибутов.

## Лабораторная работа №5
### Реализуйте полиморфизм создав основной (общий) класс “Shape”, а также еще два класса “Rectangle” и “Circle”. Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль

```python
class Shape: # определение абстрактного класса Shape (базовый класс)
  def area(self): # метод area, который должен быть переопределен в дочерних классах
    pass # пока что ничего не делает

class Rectangle(Shape): # определение класса Rectangle, наследующего от класса Shape
  def __init__(self, width, height): # метод инициализации класса Rectangle
    self.width = width # создание атрибута width и присваивание ему значения аргумента width
    self.height = height # создание атрибута height и присваивание ему значения аргумента height

  def area(self): # переопределение метода area для класса Rectangle
    return self.width * self.height # возвращает площадь прямоугольника

class Circle(Shape): # определение класса Circle, наследующего от класса Shape
  def __init__(self, radius): # метод инициализации класса Circle
    self.radius = radius # создание атрибута radius и присваивание ему значения аргумента radius

  def area(self): # переопределение метода area для класса Circle
    return 3.14 * self.radius * self.radius # возвращает площадь круга

shapes = [Rectangle(5, 4), Circle(3)] # создание списка shapes, содержащего объекты классов Rectangle и Circle

for shape in shapes: # цикл for для перебора объектов в списке shapes
  print(f"The area is: {shape.area()}") # вывод площади каждого объекта с использованием метода area()
```

### Результат.
![image](https://github.com/user-attachments/assets/32f4d227-42db-4a13-a3e0-2b3cfc98bc0b)

## Вывод
Код демонстрирует как один и тот же метод (area()) может использоваться для разных объектов с разными результатами (полиморфизм) и как абстрактные классы могут быть использованы для определения общего интерфейcа для дочерних классов.

## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def get_info(self):
        return f"Название: {self.title}\nАвтор: {self.author}\nЖанр: {self.genre}"

my_book = Book("Война и мир", "Лев Толстой", "Роман")
print(my_book.get_info())
```

### Результат.
![image](https://github.com/user-attachments/assets/b37134e1-649e-4836-b2a6-130f10298fda)

## Вывод
1. `class Book:`: Определяет класс Book для представления книги.
2. `def __init__(self, title, author, genre):`: Конструктор класса, который инициализирует объект Book атрибутами title (название), author (автор) и genre (жанр).
  - `self` - ссылка на создаваемый объект.
  - `title, author, genre` - параметры, которые будут использоваться для инициализации атрибутов.
3. `self.title = title`: Создается атрибут `title` объекта класса `Book` и ему присваивается значение параметра `title`.
4. `self.author = author`: Создается атрибут author объекта класса `Book` и ему присваивается значение параметра `author`.
5. `self.genre = genre`: Создается атрибут genre объекта класса `Book` и ему присваивается значение параметра `genre`.
6. `my_book = Book("Война и мир", "Лев Толстой", "Роман")`: Создается объект класса `Book` с именем `my_book`, передавая значения "Война и мир", "Лев Толстой" и "Роман" для атрибутов title, author и genre.
7. `print(f"Название: {my_book.title}\nАвтор: {my_book.author}\nЖанр: {my_book.genre}")`: Выводит информацию о книге в консоль, используя атрибуты объекта `my_book`.

## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Book:
 def __init__(self, title, author, genre, pages, publication_year):
  self.title = title
  self.author = author
  self.genre = genre
  self.pages = pages
  self.publication_year = publication_year

 def get_book_info(self):
  print(f"Название: {self.title}\nАвтор: {self.author}\nЖанр: {self.genre}\nКоличество страниц: {self.pages}\nГод издания: {self.publication_year}")

my_book = Book("Война и мир", "Лев Толстой", "Роман", 1225, 1869)
my_book.get_book_info()
```

### Результат.
![image](https://github.com/user-attachments/assets/c167719f-6c84-4691-8bc5-cfeeeafdc8c5)

## Вывод
1. Атрибут: `publication_year` для хранения года издания книги.
2. Метод: `get_book_info()`, который выводит информацию о книге в консоль.

## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Book:
 def __init__(self, title, author, genre, pages, publication_year):
  self.title = title
  self.author = author
  self.genre = genre
  self.pages = pages
  self.publication_year = publication_year

 def get_book_info(self):
  print(f"Название: {self.title}\nАвтор: {self.author}\nЖанр: {self.genre}\nКоличество страниц: {self.pages}\nГод издания: {self.publication_year}")

class ClassicLiterature(Book):
 def __init__(self, title, author, genre, pages, publication_year, era):
  super().__init__(title, author, genre, pages, publication_year)
  self.era = era

 def get_classic_info(self):
  print(f"Название: {self.title}\nАвтор: {self.author}\nЖанр: {self.genre}\nКоличество страниц: {self.pages}\nГод издания: {self.publication_year}\nЭпоха: {self.era}")

war_and_peace = ClassicLiterature("Война и мир", "Лев Толстой", "Роман", 1225, 1869, "XIX век")
war_and_peace.get_classic_info()
```

### Результат.
![image](https://github.com/user-attachments/assets/d38e342b-c341-4241-a4f7-cad0dc8bea74)

## Вывод
1. Создан класс `ClassicLiterature`, который наследует от `Book`. 
2. В `ClassicLiterature` добавлен новый атрибут `era`, чтобы хранить информацию о литературной эпохе.
3. Создан метод `get_classic_info()`, который выводит информацию о классическом произведении, включая эпоху.

## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Book:
 def __init__(self, title, author, genre, pages, publication_year):
  self._title = title
  self._author = author
  self._genre = genre
  self._pages = pages
  self._publication_year = publication_year

 def get_title(self):
  return self._title

 def set_title(self, title):
  self._title = title

 def get_author(self):
  return self._author

 def set_author(self, author):
  self._author = author

 def get_genre(self):
  return self._genre

 def set_genre(self, genre):
  self._genre = genre

 def get_pages(self):
  return self._pages

 def set_pages(self, pages):
  self._pages = pages

 def get_publication_year(self):
  return self._publication_year

 def set_publication_year(self, publication_year):
  self._publication_year = publication_year

 def get_book_info(self):
  print(f"Название: {self.get_title()}\nАвтор: {self.get_author()}\nЖанр: {self.get_genre()}\nКоличество страниц: {self.get_pages()}\nГод издания: {self.get_publication_year()}")

class ClassicLiterature(Book):
 def __init__(self, title, author, genre, pages, publication_year, era):
  super().__init__(title, author, genre, pages, publication_year)
  self._era = era

 def get_era(self):
  return self._era

 def set_era(self, era):
  self._era = era

 def get_classic_info(self):
  print(f"Название: {self.get_title()}\nАвтор: {self.get_author()}\nЖанр: {self.get_genre()}\nКоличество страниц: {self.get_pages()}\nГод издания: {self.get_publication_year()}\nЭпоха: {self.get_era()}")

war_and_peace = ClassicLiterature("Война и мир", "Лев Толстой", "Роман", 1225, 1869, "XIX век")
war_and_peace.get_classic_info()
```

### Результат.
![image](https://github.com/user-attachments/assets/da49f4df-a0ca-4399-b851-bd839c0ca095)

## Вывод
1. Приватные атрибуты:
  - Все атрибуты (поле) классов `Book` и `ClassicLiterature` объявлены с префиксом подчеркивания (_), например, `_title`, `_author`, `_era`. Это соглашение в Python обозначает, что эти атрибуты считаются приватными, т.е. доступными только изнутри самого класса.
  - Внешний код не может напрямую обращаться к этим атрибутам.

2. Геттеры и сеттеры:
  - Для каждого приватного атрибута определены геттеры (методы типа `get_title`, `get_author`, `get_era`) и сеттеры (методы типа `set_title`, `set_author`, `set_era`).
  - Геттеры предоставляют возможность получения значения приватного атрибута, а сеттеры - изменения его значения.
  
## Самостоятельная работа №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Book:
 def __init__(self, title, author, genre, pages, publication_year):
  self._title = title
  self._author = author
  self._genre = genre
  self._pages = pages
  self._publication_year = publication_year

 def get_title(self):
  return self._title

 def set_title(self, title):
  self._title = title

 def get_author(self):
  return self._author

 def set_author(self, author):
  self._author = author

 def get_genre(self):
  return self._genre

 def set_genre(self, genre):
  self._genre = genre

 def get_pages(self):
  return self._pages

 def set_pages(self, pages):
  self._pages = pages

 def get_publication_year(self):
  return self._publication_year

 def set_publication_year(self, publication_year):
  self._publication_year = publication_year

 def get_book_info(self):
  print(f"Название: {self.get_title()}\nАвтор: {self.get_author()}\nЖанр: {self.get_genre()}\nКоличество страниц: {self.get_pages()}\nГод издания: {self.get_publication_year()}")

class ClassicLiterature(Book):
 def __init__(self, title, author, genre, pages, publication_year, era):
  super().__init__(title, author, genre, pages, publication_year)
  self._era = era

 def get_era(self):
  return self._era

 def set_era(self, era):
  self._era = era

 def get_classic_info(self):
  print(f"Название: {self.get_title()}\nАвтор: {self.get_author()}\nЖанр: {self.get_genre()}\nКоличество страниц: {self.get_pages()}\nГод издания: {self.get_publication_year()}\nЭпоха: {self.get_era()}")

class ModernNovel(Book):
 def __init__(self, title, author, genre, pages, publication_year, awards):
  super().__init__(title, author, genre, pages, publication_year)
  self._awards = awards

 def get_awards(self):
  return self._awards

 def set_awards(self, awards):
  self._awards = awards

 def get_modern_info(self):
  print(f"Название: {self.get_title()}\nАвтор: {self.get_author()}\nЖанр: {self.get_genre()}\nКоличество страниц: {self.get_pages()}\nГод издания: {self.get_publication_year()}\nНаграды: {self.get_awards()}")

books = [
  ClassicLiterature("Война и мир", "Лев Толстой", "Роман", 1225, 1869, "XIX век"),
  ModernNovel("1984", "Джордж Оруэлл", "Антиутопия", 328, 1949, "Премия памяти Джона У. Кэмпбелла")
]

for book in books:
 if isinstance(book, ClassicLiterature):
  book.get_classic_info()
 elif isinstance(book, ModernNovel):
  book.get_modern_info()
```

### Результат.
![image](https://github.com/user-attachments/assets/1c217865-b1f4-4c1a-9863-69461bdecdc9)

## Вывод
В коде реализован полиморфизм через:
1. Разные методы для вывода информации: Методы `get_classic_info()` и `get_modern_info()` отличаются по выводимой информации.
2. Единый интерфейс: Несмотря на разные методы, все книги вызывают метод `get_book_info()` для вывода общей информации.

## Общие выводы по теме
Ключевые концепции ООП в Python:
1. Классы: Шаблоны для создания объектов, которые определяют атрибуты и методы.
2. Объекты: Конкретные экземпляры класса, которые содержат данные и могут выполнять действия.
3. Инкапсуляция: Скрытие данных и методов внутри класса, обеспечивая доступ к ним только через определенные интерфейсы (геттеры и сеттеры).
4. Наследование: Создание нового класса (дочерний класс) на основе существующего класса (родительский класс), наследуя его атрибуты и методы.
5. Полиморфизм: Использование одного и того же имени метода для разных объектов, с различной реализацией в зависимости от типа объекта.
