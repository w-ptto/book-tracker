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

def add_book():
    books = load_books()
    author = input("Введите имя автора книги:")
    title = input ("Введите название книги:")

    for book in books:
        if book["author"].lower() == author.lower() and book["title"].lower() == title.lower():
            print("Такая книга уже существует.")
            return

    while True:
        try:
            rating = int(input("Введите оценку (1-5): "))

            if 1 <= rating <= 5:
                break

            print("Оценка должна быть от 1 до 5.")

        except ValueError:
            print("Введите число.")

    read_date = input("Введите дату прочтения: ")

    new_book = {
        "author": author,
        "title": title,
        "rating": rating,
        "date": read_date
    }

    books.append(new_book)

    save_books(books)

    print("Книга добавлена.")
