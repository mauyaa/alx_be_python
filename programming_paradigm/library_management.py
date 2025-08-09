class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print(f"Book added: '{title}' by {author}")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_borrowed:
                    print(f"'{title}' is already borrowed.")
                else:
                    book.is_borrowed = True
                    print(f"You borrowed '{title}'.")
                return
        print(f"'{title}' not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f"You returned '{title}'.")
                else:
                    print(f"'{title}' was not borrowed.")
                return
        print(f"'{title}' not found in the library.")
