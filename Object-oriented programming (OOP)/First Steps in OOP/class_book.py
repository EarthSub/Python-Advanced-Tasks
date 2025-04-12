# Create a class called Book. It should have an __init__() method that should receive:

#     · name: string
#     · author: string
#     · pages: int

# Submit only the class in the judge system.


#                         Examples

# Test Code                                           Output

# book = Book("My Book", "Me", 200)                   My Book
# print(book.name)                                    Me
# print(book.author)                                  200
# print(book.pages)


class Book:
    def __init__(self, name, author,pages):
        self.name = name
        self.author = author
        self.pages = pages



book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)