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
