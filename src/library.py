import json
import os
from typing import List
from .book import Book

class Library:
    def __init__(self):
        self.books = []
        self.last_id = 0
        self.filename = "library.json"

    def add_book(self, title: str, author: str, year: int) -> None:
        """Добавляет новую книгу в библиотеку"""
        book = Book(title, author, year)
        self.last_id = max([b.id for b in self.books] + [0]) + 1
        book.id = self.last_id
        self.books.append(book)
        self.save_books()
        print(f"Книга '{title}' успешно добавлена с ID {book.id}")

    def find_book_by_id(self, book_id: int) -> Book:
        """Находит книгу по ID"""
        return next((book for book in self.books if book.id == book_id), None)

    def remove_book(self, book_id: int) -> None:
        """Удаляет книгу из библиотеки по ID"""
        book = self.find_book_by_id(book_id)
        if book:
            self.books = [b for b in self.books if b.id != book_id]
            self.save_books()
            print(f"Книга с ID {book_id} успешно удалена")
        else:
            print(f"Книга с ID {book_id} не найдена")

    def save_books(self):
        """Сохраняет книги в JSON файл"""
        with open(self.filename, "w") as f:
            json.dump([book.to_dict() for book in self.books], f, indent=2)

    def load_books(self):
        """Загружает книги из JSON файла"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    data = json.load(f)
                    self.books = []
                    for book_data in data:
                        book = Book(
                            title=book_data['title'],
                            author=book_data['author'],
                            year=book_data['year'],
                            id=book_data['id'],
                            status=book_data['status']
                        )
                        self.books.append(book)
                    if self.books:
                        self.last_id = max(book.id for book in self.books)
            except json.JSONDecodeError:
                self.books = []
                self.last_id = 0
            except KeyError as e:
                self.books = []
                self.last_id = 0
        else:
            self.books = []
            self.last_id = 0

    def search_books(self, query: str) -> List[Book]:
        """Ищет книги по названию, автору или году"""
        query = query.lower()
        return [book for book in self.books if
                query in book.title.lower() or
                query in book.author.lower() or
                query == str(book.year)]

    def display_all_books(self) -> None:
        """Отображает все книги в библиотеке"""
        if not self.books:
            print("Библиотека пуста")
        else:
            for book in self.books:
                print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, "
                      f"Год: {book.year}, Статус: {book.status}")

    def change_book_status(self, book_id: int, new_status: str) -> None:
        """Изменяет статус книги"""
        book = self.find_book_by_id(book_id)
        if book:
            if new_status in ["в наличии", "выдана"]:
                book.status = new_status
                self.save_books()
                print(f"Статус книги с ID {book_id} изменен на '{new_status}'")
            else:
                print("Некорректный статус. Используйте 'в наличии' или 'выдана'")
        else:
            print(f"Книга с ID {book_id} не найдена")