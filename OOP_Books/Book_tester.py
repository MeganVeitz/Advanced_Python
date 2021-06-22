from Ex1_OOPBooks import Book, Author

print("Making an Author:")
author1 = Author("James", "Lucky", "Bismarck")
print(author1)
print("Making a Book:")
book1 = Book("Brisk", 1955, 485)
print(book1)
print("Adding a Book:")
author1.add_book(book1)
print(author1)
