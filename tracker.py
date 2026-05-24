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

def show_books():
    books = load_books()

    if not books:
        print("Список книг пуст.")
        return

    print("\nСписок книг:")

    for index, book in enumerate(books, start=1):
        print(
            f"{index}. "
            f"{book['author']} — "
            f"{book['title']} | "
            f"Оценка: {book['rating']} | "
            f"Дата: {book['date']}"
        )