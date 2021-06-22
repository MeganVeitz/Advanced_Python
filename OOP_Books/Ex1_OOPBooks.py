# Meg Veitz
# 3/23/21
class Author:
    def __init__(self, fname, lname, birth_place):
        self.fname = fname
        self.lname = lname
        self.birth_place = birth_place
        self.books = []

    def __str__(self):
        return f"{self.fname} {self.lname} was born in {self.birth_place} \nThey currently have {len(self.books)} book(s)."

    def add_book(self, book):
        self.books.append(book)

class Book:
    def __init__(self, title, publish_date, pages):
        self.title = title
        self.publish_date = publish_date
        self.pages = pages

    def __str__(self):
        return f"The book {self.title} was published in {self.publish_date} and has {self.pages} pages."
