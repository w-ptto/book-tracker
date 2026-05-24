import json
import os

FILE_NAME = "books.json"


def load_books():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_books(books):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)

def delete_book():
    books = load_books()

    if not books:
        print("Список пуст.")
        return

    show_books()

    try:
        index = int(input("Введите номер книги для удаления: ")) - 1

        if 0 <= index < len(books):
            removed = books.pop(index)

            save_books(books)

            print(
                f"Удалена книга: "
                f"{removed['author']} — {removed['title']}"
            )
        else:
            print("Неверный номер.")

    except ValueError:
        print("Введите число.")
