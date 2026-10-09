
# Library Management System

books = [
    {"title": "Python Basics", "author": "John", "available": True},
    {"title": "Java Programming", "author": "Smith", "available": True},
    {"title": "Web Development", "author": "David", "available": True},
    {"title": "Database Systems", "author": "Mary", "available": True},
    {"title": "Computer Networks", "author": "Alex", "available": True}
]

def search_book(title):
    for book in books:
        if book["title"].lower() == title.lower():
            return book
    raise ValueError("Book does not exist.")

def borrow_book(title):
    book = search_book(title)

    if not book["available"]:
        print("This book is already borrowed.")
    else:
        book["available"] = False
        print("Book borrowed successfully.")

def return_book(title):
    book = search_book(title)

    if book["available"]:
        print("This book was not borrowed.")
    else:
        book["available"] = True
        print("Book returned successfully.")

def display_books():
    print("\nAvailable Books:")
    for book in books:
        if book["available"]:
            print(book["title"], "-", book["author"])

while True:
    print("\n1. Search Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Display Available Books")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 5:
            break

        if choice == 4:
            display_books()
            continue

        title = input("Enter book title: ")

        if choice == 1:
            book = search_book(title)
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Available:", book["available"])

        elif choice == 2:
            borrow_book(title)

        elif choice == 3:
            return_book(title)

        else:
            print("Invalid menu choice.")

    except ValueError as error:
        print("Error:", error)