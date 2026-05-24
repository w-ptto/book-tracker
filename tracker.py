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

#############################

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


######################################

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


def average_rating():
    books = load_books()

    if not books:
        print("Нет книг для расчёта.")
        return

    avg = sum(book["rating"] for book in books) / len(books)

    print(f"Средняя оценка: {avg:.2f}")


def author_stats():
    books = load_books()

    if not books:
        print("Нет данных.")
        return

    stats = {}

    for book in books:
        author = book["author"]

        if author in stats:
            stats[author] += 1
        else:
            stats[author] = 1

    print("\nСтатистика по авторам:")

    for author, count in stats.items():
        print(f"{author}: {count} книг")

#############################

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


###############


def main():
    while True:
        print("\nТрекер прочитанных книг")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            show_books()

        elif choice == "3":
            average_rating()

        elif choice == "4":
            author_stats()

        elif choice == "5":
            delete_book()

        elif choice == "6":
            print("Выход из программы.")
            break

        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    main()