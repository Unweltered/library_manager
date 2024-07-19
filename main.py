from src.library import Library

def main():
    library = Library()

    while True:
        library.load_books()
        print("\n--- Меню ---")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания: "))
            library.add_book(title, author, year)

        elif choice == "2":
            book_id = int(input("Введите ID книги для удаления: "))
            library.remove_book(book_id)

        elif choice == "3":
            query = input("Введите название, автора или год книги: ")
            results = library.search_books(query)
            if results:
                print("Результаты поиска:")
                for book in results:
                    print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, "
                          f"Год: {book.year}, Статус: {book.status}")
            else:
                print("Книги не найдены")

        elif choice == "4":
            library.display_all_books()

        elif choice == "5":
            book_id = int(input("Введите ID книги для изменения статуса: "))
            new_status = input("Введите новый статус (в наличии/выдана): ")
            library.change_book_status(book_id, new_status)

        elif choice == "0":
            print("До свидания!")
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()