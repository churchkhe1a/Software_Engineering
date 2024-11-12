class LogDecorator: # Декоратор, который выводит информацию о вызове декорированной функции

  def __init__(self, func): # Инициализирует декоратор, запоминает декорируемую функцию
    self.func = func

  def __call__(self, *args, **kwargs): # Выполняется при вызове декорированной функции
    print(f"Вызов функции: {self.func.__name__}")
    print(f"Аргументы: {args}, {kwargs}")
    result = self.func(*args, **kwargs) # Выполняем декорируемую функцию
    print(f"Результат: {result}")
    print(f"Функция {self.func.__name__} завершена")
    return result


@LogDecorator
def greet(name): # Приветствует пользователя по имени
  return f"Привет, {name}!"

@LogDecorator
def calculate_sum(a, b): # Складывает два числа
  return a + b

if __name__ == '__main__':
  greet("Саша")
  print()
  calculate_sum(10, 20)
