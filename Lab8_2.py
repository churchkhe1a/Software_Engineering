class Car: # определение класса Car
  def __init__(self, make, model): # метод инициализации класса (конструктор)
    self.make = make # создание атрибута make и присваивание ему значения аргумента make
    self.model = model # создание атрибута model и присваивание ему значения аргумента model

  def drive(self): # метод класса для имитации вождения
    print(f"Driving the {self.make} {self.model}") # вывод сообщения о вождении автомобиля

my_car = Car("Toyota", "Corolla") # создание объекта класса Car с именем my_car,
                 # передавая в конструктор значения "Toyota" и "Corolla" для атрибутов make и model
my_car.drive() # вызов метода drive() для объекта my_car
