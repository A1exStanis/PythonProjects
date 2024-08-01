class Book:
    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year

    def __str__(self):
        return f'Title: {self.title}'


class Author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def __str__(self):
        return f'Autor: {self.name}, born: {self.birth_year}'


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]

    def find_book_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def __str__(self):
        book_str = '\n'.join(str(book) for book in self.books)
        return f'Library: {self.name}.\nBooks:\n{book_str if book_str else 'Library is empty'}'


book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 1925)
book2 = Book("1984", "George Orwell", "9780451524935", 1949)
author = Author("George Orwell", 1903)

# Створення бібліотеки та додавання книг
library = Library("City Library")
library.add_book(book1)
library.add_book(book2)

# Пошук книги
print(library.find_book_by_title("1984"))

# Видалення книги
library.remove_book("9780743273565")

# Виведення інформації про бібліотеку
print(library)

print("Search Results for '1984':")
for book in library.find_book_by_title("1984"):
    print(book)
