import json
from datetime import datetime
FILE_NAME = "books.json"

# Работа с файлом

def load_books():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_books(books):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)


# Функции приложения

def add_book():
    books = load_books()
    author = input("Введите автора: ").strip()
    title = input("Введите название: ").strip()

    # Проверка дубликатов
    for book in books:
        if book["author"].lower() == author.lower() and book["title"].lower() == title.lower():
            print("Такая книга уже есть")
            return

    # Валидация оценки
    while True:
        try:
            rating = int(input("Введите оценку (1-5): "))
            if 1 <= rating <= 5:
                break
            else:
                print("Оценка должна быть от 1 до 5")
        except ValueError:
            print("Введите число")

    # Валидация даты
    while True:
        date = input("Введите дату (YYYY-MM-DD): ")
        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Неверный формат даты")
    books.append({
        "author": author,
        "title": title,
        "rating": rating,
        "date": date
    })

    save_books(books)
    print("Книга добавлена")

def list_books():
    books = load_books()
    if not books:
        print("Список пуст")
        return
    print("\nСписок книг:")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book['author']} — {book['title']} | Оценка: {book['rating']} | Дата: {book['date']}")
def average_rating():
    books = load_books()
    if not books:
        print("Нет данных")
        return
    avg = sum(book["rating"] for book in books) / len(books)
    print(f"Средняя оценка: {avg:.2f}")
def stats_by_author():
    books = load_books()
    if not books:
        print("Нет данных")
        return
    stats = {}
    for book in books:
        author = book["author"]
        stats[author] = stats.get(author, 0) + 1
    print("\nСтатистика по авторам:")
    for author, count in stats.items():
        print(f"{author}: {count} книг(и)")
def delete_book():
    books = load_books()
    if not books:
        print("Список пуст")
        return
    list_books()
    try:
        index = int(input("Введите номер книги для удаления: ")) - 1
        if 0 <= index < len(books):
            removed = books.pop(index)
            save_books(books)
            print(f"Удалено: {removed['author']} — {removed['title']}")
        else:
            print("Неверный номер")
    except ValueError:
        print("Введите число")

# Меню
def show_menu():
    print("\n===== Трекер книг =====")
    print("1. Добавить книгу")
    print("2. Показать все книги")
    print("3. Показать среднюю оценку")
    print("4. Статистика по авторам")
    print("5. Удалить книгу")
    print("6. Выход")
def main():
    while True:
        show_menu()
        choice = input("Выберите пункт: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            list_books()
        elif choice == "3":
            average_rating()
        elif choice == "4":
            stats_by_author()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            print("Выход из программы")
            break
        else:
            print("Неверный выбор")
if __name__ == "__main__":
    main()
