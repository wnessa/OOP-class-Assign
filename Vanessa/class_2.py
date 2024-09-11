# Class: Book
class Book:
    # Constructor method with attributes: title, author, pages
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Method: read
    def read(self):
        return f"Reading '{self.title}' by {self.author}."

    # Method: bookmark_page
    def bookmark_page(self, page):
        return f"Bookmarked page {page} in '{self.title}'."
