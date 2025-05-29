class Media:
    def borrow(self, user_id):
        pass

    def read(self):
        pass

    def listen(self):
        pass


class Book(Media):
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

    def listen(self):
        pass


class EBook(Media):
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

    def listen(self):
        pass


class Audiobook(Media):
    def __init__(self):
        self.borrowed = False
        self.progress = 0

    def borrow(self, user_id):
        self.borrowed = True
        print(f"Audiobook borrowed by user {user_id}.")

    def read(self):
        pass

    def listen(self):
        if self.borrowed:
            self.progress += 15
            print(f"Listening to the audiobook. Progress: {self.progress}%")
        else:
            print("Audiobook must be borrowed first.")


book = Book()
book.borrow("user123")
book.read()
book.listen()  # No effect, but must be present

ebook = EBook()
ebook.borrow("user456")
ebook.read()
ebook.listen()  # No effect, but must be present

audiobook = Audiobook()
audiobook.borrow("user789")
audiobook.read()  # No effect, but must be present
audiobook.listen()
