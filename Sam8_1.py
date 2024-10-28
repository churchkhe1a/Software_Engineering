class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def get_info(self):
        return f"Название: {self.title}\nАвтор: {self.author}\nЖанр: {self.genre}"

my_book = Book("Война и мир", "Лев Толстой", "Роман")
print(my_book.get_info())
