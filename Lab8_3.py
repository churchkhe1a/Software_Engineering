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
