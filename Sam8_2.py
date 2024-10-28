class Book:
 def __init__(self, title, author, genre, pages, publication_year):
  self.title = title
  self.author = author
  self.genre = genre
  self.pages = pages
  self.publication_year = publication_year

 def get_book_info(self):
  print(f"Название: {self.title}\nАвтор: {self.author}\nЖанр: {self.genre}\nКоличество страниц: {self.pages}\nГод издания: {self.publication_year}")

my_book = Book("Война и мир", "Лев Толстой", "Роман", 1225, 1869)
my_book.get_book_info()
