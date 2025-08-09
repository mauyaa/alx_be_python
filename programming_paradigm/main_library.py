from library_management import Library

# Create a library instance
lib = Library()

# Add some books
lib.add_book("The Great Gatsby", "F. Scott Fitzgerald")
lib.add_book("1984", "George Orwell")

# Show all books
print("\n--- All Books ---")
lib.display_books()

# Borrow a book
print("\n--- Borrow '1984' ---")
lib.borrow_book("1984")

# Try borrowing the same book again
lib.borrow_book("1984")

# Return a book
print("\n--- Return '1984' ---")
lib.return_book("1984")

# Display books again
print("\n--- Updated Book List ---")
lib.display_books()
