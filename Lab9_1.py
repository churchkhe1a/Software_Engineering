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
