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
