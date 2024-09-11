# Class: Library
class Library:
    # Constructor method with attribute: name
    def __init__(self, name):
        self.name = name
        self.books = []

    # Method: add_book
    def add_book(self, book):
        self.books.append(book)

    # Method: library_info
    def library_info(self):
        return f"Library: {self.name}, Number of Books: {len(self.books)}"
