import unittest
from src.book import Book

class TestBook(unittest.TestCase):
    def test_book_creation(self):
        book = Book("Test Title", "Test Author", 2023)
        self.assertEqual(book.title, "Test Title")
        self.assertEqual(book.author, "Test Author")
        self.assertEqual(book.year, 2023)
        self.assertEqual(book.status, "в наличии")
        self.assertIsNone(book.id)

if __name__ == '__main__':
    unittest.main()