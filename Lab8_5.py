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
