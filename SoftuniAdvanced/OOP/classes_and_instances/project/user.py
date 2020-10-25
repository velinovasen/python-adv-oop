from SoftuniAdvanced.OOP.classes_and_instances.project.library import *


class User:
    books = []

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username

    def get_book(self, author, book_name, days_to_return, library):
        ll = [[k, v] for k, v in library.rented_books.items()]
        days_t = 0
        for x in ll:
            if book_name in x[1]:
                days_t = x[1][book_name]
                return f"The book \"{book_name}\" is already rented and will be available in {days_t} days!"

        if author in library.books_available:
            if book_name in library.books_available[author]:
                library.books_available[author].remove(book_name)
                library.rented_books[self.username] = {"book_name": days_to_return}
                self.books.append(book_name)
                return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author, book_name, library: Library):
        if book_name not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"
        del library.rented_books[self.username][book_name]
        library.books_available[author].append(book_name)
        self.books.remove(book_name)

    def info(self):
        return f"{', '.join(sorted(self.books))}"

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"
