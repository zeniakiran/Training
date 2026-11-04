# ── BOOK CLASS ─────────────────────────────────────────────────

# Define the Book class
class Book:

    # Initialize book details
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    # Borrow a book
    def borrow(self):
        if self.is_borrowed == True:
            print("Sorry, this book is already borrowed!")
        else:
            self.is_borrowed = True
            print("You have borrowed:", self.title)

    # Return a book
    def return_book(self):
        if self.is_borrowed == False:
            print("This book was not borrowed!")
        else:
            self.is_borrowed = False
            print("You have returned:", self.title)

    # Display book information
    def __str__(self):
        if self.is_borrowed == True:
            status = "Borrowed"
        else:
            status = "Available"

        return "{} by {} [{}]".format(self.title, self.author, status)


# ── LIBRARY ────────────────────────────────────────────────────

# Create book objects
book1 = Book("Python Basics", "John Smith")
book2 = Book("Learn Java", "David Lee")
book3 = Book("Web Development", "Sarah Jones")

print("=" * 42)
print("          LIBRARY MANAGEMENT")
print("=" * 42)

# Display all books
print(book1)
print(book2)
print(book3)

print("\n--- Borrowing Books ---")

# Borrow books
book1.borrow()
book2.borrow()

# Try borrowing the same book again
book1.borrow()

print("\n--- Returning Books ---")

# Return a borrowed book
book1.return_book()

# Try returning a book that was never borrowed
book3.return_book()

print("\n--- Updated Book Status ---")

# Display books with updated status
print(book1)
print(book2)
print(book3)