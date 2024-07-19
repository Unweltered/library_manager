import unittest
import os
from src.library import Library
from src.book import Book

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.library.filename = "test_library.json"

    def tearDown(self):
        if os.path.exists(self.library.filename):
            os.remove(self.library.filename)

    def test_add_book(self):
        self.library.add_book("Test Book", "Test Author", 9999)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Test Book")

    def test_remove_book(self):
        self.library.add_book("Test Book", "Test Author", 9999)
        book_id = self.library.books[0].id
        self.library.remove_book(book_id)
        self.assertEqual(len(self.library.books), 0)

    def test_find_book_by_id(self):
        self.library.add_book("Test Book", "Test Author", 9999)
        book_id = self.library.books[0].id
        found_book = self.library.find_book_by_id(book_id)
        self.assertIsNotNone(found_book)
        self.assertEqual(found_book.title, "Test Book")

    def test_search_books(self):
        self.library.add_book("Python Book", "Test Autor", 9999)
        self.library.add_book("Java Book", "Test Autor", 9999)
        results = self.library.search_books("Python")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Python Book")

    def test_change_book_status(self):
        self.library.add_book("Test Book", "Test Author", 9999)
        book_id = self.library.books[0].id
        self.library.change_book_status(book_id, "выдана")
        self.assertEqual(self.library.books[0].status, "выдана")

if __name__ == '__main__':
    unittest.main()