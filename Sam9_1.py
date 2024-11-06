class Tomato: # Класс, представляющий томат

    states = ["отсутствует", "цветение", "зеленый", "красный"]  # Стадии созревания

    def __init__(self, index): # Инициализирует томат
        self._index = index  # Индекс томата, приватное свойство
        self._state = self.states[0] # Начальная стадия созревания, приватное свойство

    def grow(self): # Переводит томат на следующую стадию созревания
        current_state_index = self.states.index(self._state) # Находим индекс текущей стадии
        if current_state_index < len(self.states) - 1: # Проверяем, есть ли следующая стадия
            self._state = self.states[current_state_index + 1] # Переходим на следующую стадию

    def is_ripe(self): # Проверяет, созрел ли томат
        return self._state == "красный"


class TomatoBush: # Класс, представляющий куст с помидорами

    def __init__(self, num_tomatoes): #Инициализирует куст с заданным количеством томатов
        self.tomatoes = [Tomato(i) for i in range(num_tomatoes)] # Создаем список томатов

    def grow_all(self): # Переводит все томаты на кусте на следующую стадию созревания
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self): # Проверяет, все ли томаты на кусте созрели
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self): # Удаляет все томаты с куста после сбора урожая
        self.tomatoes = []


class Gardener: # Класс, представляющий садовника

    def __init__(self, name, plant): # Инициализирует садовника
        self.name = name  # Имя садовника, публичное свойство
        self._plant = plant # Объект TomatoBush, растение, приватное свойство

    def work(self): # Садовник ухаживает за кустом, заставляя томаты расти
        self._plant.grow_all()

    def harvest(self): # Садовник собирает урожай, если все томаты созрели
        if self._plant.all_are_ripe(): # Проверяем, созрели ли все томаты
            self._plant.give_away_all() # Сбор урожая
            print(f"Садовник {self.name} собрал урожай!")
        else:
            print(f"Садовник {self.name}: Помидоры еще не созрели!")

    @staticmethod
    def knowledge_base(): # Выводит справку по садоводству
        print("Справка по садоводству: \n"
              "Помидоры растут постепенно, от отсутствия до красного цвета.\n"
              "Ухаживайте за ними и они порадуют вас вкусным урожаем.")


# Тесты
Gardener.knowledge_base()  # Вызов справки по садоводству
print()

bush = TomatoBush(5)  # Создание куста с 5 помидорами
gardener = Gardener("Иван", bush)  # Создание садовника Ивана

print("Уход за кустом:")
for _ in range(3):  # Симуляция роста в течение 3 дней
    gardener.work()
    print(f"Томаты на кусте: {[tomato._state for tomato in bush.tomatoes]}")
print()

print("Попытка сбора урожая:")
gardener.harvest()
print()

print("Продолжение ухода:")
for _ in range(2):  # Симуляция роста в течение 2 дней
    gardener.work()
    print(f"Томаты на кусте: {[tomato._state for tomato in bush.tomatoes]}")
print()

print("Сбор урожая:")
gardener.harvest()
