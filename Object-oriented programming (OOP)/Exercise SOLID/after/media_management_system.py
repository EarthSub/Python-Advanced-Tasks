# DONE


from abc import ABC, abstractmethod


class Borrowable(ABC):

    def borrow(self, user_id):
        pass


class Readable(ABC):

    @abstractmethod
    def read(self):
        pass


class Listenable(ABC):

    @abstractmethod
    def listen(self):
        pass


class Book(Borrowable, Readable):
    def __init__(self):
        self.borrowed = False
        self.progress = 0

    def borrow(self, user_id):
        self.borrowed = True
        print(f"Book borrowed by user {user_id}.")

    def read(self):
        if self.borrowed:
            self.progress += 10
            print(f"Reading the book. Progress: {self.progress}%")
        else:
            print("Book must be borrowed first.")


class EBook(Borrowable, Readable):
    def __init__(self):
        self.borrowed = False
        self.drm_applied = False
        self.progress = 0

    def borrow(self, user_id):
        self.drm_applied = True
        self.borrowed = True
        print(f"eBook borrowed by user {user_id}. DRM applied.")

    def read(self):
        if self.borrowed:
            self.progress += 20
            print(f"Reading the eBook. Progress: {self.progress}%")
        else:
            print("eBook must be borrowed first.")


class Audiobook(Borrowable, Listenable):
    def __init__(self):
        self.borrowed = False
        self.progress = 0

    def borrow(self, user_id):
        self.borrowed = True
        print(f"Audiobook borrowed by user {user_id}.")

    def listen(self):
        if self.borrowed:
            self.progress += 15
            print(f"Listening to the audiobook. Progress: {self.progress}%")
        else:
            print("Audiobook must be borrowed first.")



book = Book()
book.borrow("user123")
book.read()


try:
    book.listen()
except AttributeError as e:
    print(e)


ebook = EBook()
ebook.borrow("user456")
ebook.read()


try:
    ebook.listen()
except AttributeError as e:
    print(e)


audiobook = Audiobook()
audiobook.borrow("user789")
audiobook.listen()


try:
    audiobook.read()
except AttributeError as e:
    print(e)
