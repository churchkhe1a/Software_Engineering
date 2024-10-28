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
