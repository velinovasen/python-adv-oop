class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self, location):
        self.location = location
        self.books = []

    def find_book(self, title):
        if title in [x.title for x in self.books]:
            return f"Found it"
        return f'We don\'t have this book'

    def add_book(self, book):
        self.books.append(book)