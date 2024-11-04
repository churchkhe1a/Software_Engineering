# Тема 8. Концепции и принципы ООП.
Отчет по Теме #9 выполнил(а):
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
### Допустим, что вы решили оригинально и немного странно познакомится с человеком. Для этого у вас должен быть написан свой класс на Python, который будет проверять угадал ваше имя человек или нет. Для этого создайте класс, указав в свойствах только имя. Дальше создайте функцию init(), а в ней сделайте проверку на то угадал человек ваше имя или нет. Также можете проверить что будет, если в этой функции указав атрибут, который не указан в вашем классе, например, попробуйте вызвать фамилию.

```python
class Sasha:
    __slots__ = ['name']

    def __init__(self, name):
        if name == 'Саша':
            self.name = f"Да, я {name}"
        else:
            self.name = f"Я не {name}, а Саша"

person1 = Sasha('Иван')
person2 = Sasha('Саша')
print(person1.name)
print(person2.name)
person2.surname = 'Обласова'
```

### Результат.


## Вывод
1. `def __init__(self, make, model):`: Определяет специальный метод `__init__`, который является конструктором класса. Он вызывается автоматически при создании нового объекта этого класса.
2. `self` - ссылка на создаваемый объект.
3. `make` и `model` - параметры, которые будут использоваться для инициализации атрибутов.
4. `self.make = make`: Создается атрибут make объекта класса `Car` и ему присваивается значение параметра `make`.
5. `self.model = model`: Создается атрибут model объекта класса `Car` и ему присваивается значение параметра `model`.
6. `my_car = Car("Toyota", "Corolla")`: Создается объект класса `Car` с именем `my_car`. При создании объекта в конструктор передаются значения "Toyota" и "Corolla" для атрибутов `make` и `model`.
Этот код демонстрирует создание класса в Python. Класс - это blueprint для создания объектов с определенными атрибутами (характеристиками). В этом случае мы создали класс для представления автомобиля с атрибутами "марка" и "модель".

## Лабораторная работа №2
### Вам дали важное задание, написать продавцу мороженого программу, которая будет писать добавили ли топпинг в мороженое и цену после возможного изменения. Для этого вам нужно написать класс, в котором будет определяться изменили ли состав мороженого или нет. В этом классе реализуйте метод, выводящий на печать «Мороженое с {ТОППИНГ}» в случае наличия добавки, а иначе отобразится следующая фраза: «Обычное мороженое». При этом программа должна воспринимать как топпинг только атрибуты типа string.

```python
class Icecream:
    def __init__(self, ingredient=None):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def composition(self):
        if self.ingredient:
            print(f"Мороженое с {self.ingredient}")
        else:
            print('Обычное мороженое')
            
icecream = Icecream()
icecream.composition()
icecream = Icecream('шоколадом')
icecream.composition()
icecream = Icecream(5)
icecream.composition()
```

### Результат.


## Вывод
1. Добавлен метод `drive()`, который имитирует действие "езда" и выводит сообщение.
2. Вызов метода `drive()` для объекта `my_car` заставляет машину "поехать".
Код демонстрирует работу класса с методом, который имитирует действие.

## Лабораторная работа №3
### Петя – начинающий программист и на занятиях ему сказали реализовать икапсу…что-то. А вы хороший друг Пети и ко всему прочему прекрасно знаете, что икапсу…что-то – это инкапсуляция, поэтому решаете помочь вашему другу с написанием класса с инкапсуляцией. Ваш класс будет не просто инкапсуляцией, а классом с сеттером, геттером и деструктором. После написания класса вам необходимо продемонстрировать что все написанные вами функции работают. Также вас необходимо объяснить Пете почему на скриншоте ниже в консоли выводится ошибка.

```python
class MyClass:
    def __init__(self, value):
        self._value = value

    def set_value(self, value):
        self._value = value

    def get_value(self):
        if hasattr(self, '_value'):
            return self._value
        else:
            raise AttributeError("Значение удалено")

    def del_value(self):
        del self._value

    value = property(get_value, set_value, del_value, "Свойство value")


obj = MyClass(42)
print(obj.value)
obj.set_value(45)
print(obj.value)
obj.set_value(100)
print(obj.value)
obj.del_value()
try:
    print(obj.value)
except AttributeError as e:
    print(e)
```
# Проблема была в том что метод get_value принимал value, и в том что после удаления value, мы пытались вывести value без проверки его удаления.


### Результат.


## Вывод
Этот код демонстрирует как можно использовать наследование для создания новых классов, расширяющих функциональность существующих классов. Он также демонстрирует как методы могут вести себя по-разному в разных классах (полиморфизм).

## Лабораторная работа №4
### Вам прекрасно известно, что кошки и собаки являются млекопитающими, но компьютер этого не понимает, поэтому вам нужно написать три класса: Кошки, Собаки, Млекопитающие. И при помощи “наследования” объяснить компьютеру что кошки и собаки – это млекопитающие. Также добавьте какой-нибудь свой атрибут для кошек и собак, чтобы показать, что они чем-то отличаются друг от друга.

```python
class Mammal:
    className = 'Mammal'


class Dog(Mammal):
    species = 'canine'
    sounds = 'wow'


class Cat(Mammal):
    species = 'feline'
    sounds = 'meow'


dog = Dog()
print(f"Dog is {dog.className}, but they say {dog.sounds}")
cat = Cat()
print(f"Cat is {cat.className}, but they say {cat.sounds}")
```

### Результат.

## Вывод
1. `my_car = Car("Toyota", "Corolla")`: Создает объект класса `Car` с именем `my_car`, передавая значения "Toyota" и "Corolla".
2. `my_car.drive()`: Вызывает метод `drive()`, который выводит сообщение о вождении автомобиля.
Код демонстрирует, как реализовать инкапсуляцию в Python, используя соглашения о наименовании для создания защищенных и приватных атрибутов.

## Лабораторная работа №5
### На разных языках здороваются по-разному, но суть остается одинаковой, люди друг с другом здороваются. Давайте вместе с вами реализуем программу с полиморфизмом, которая будет описывать всю суть первого предложения задачи. Для этого мы можем выбрать два языка, например, русский и английский и написать для них отдельные классы, в которых будет в виде атрибута слово, которым здороваются на этих языках. А также напишем функцию, которая будет выводить информацию о том, как на этих языках здороваются. Заметьте, что для решения поставленной задачи мы использовали декоратор @staticmethod, поскольку нам не нужны обязательные параметры-ссылки вроде self.

```python
class Russian:
    @staticmethod
    def greeting():
        print("Привет")


class English:
    @staticmethod
    def greeting():
        print("Hello")


def greet(language):
    language.greeting()


ivan = Russian()
greet(ivan)
john = English()
greet(john)
```

### Результат.


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


## Вывод
В коде реализован полиморфизм через:
1. Разные методы для вывода информации: Методы `get_classic_info()` и `get_modern_info()` отличаются по выводимой информации.
2. Единый интерфейс: Несмотря на разные методы, все книги вызывают метод `get_book_info()` для вывода общей информации.

## Общие выводы по теме

