from schemas.book import bookcreate

class bookservice:
    def __init__(self):
        self.book = []
        self.next_id = 1

    def get_all_books(self):
        return self.book

    def add_book(self,book_data :bookcreate):
        new_book = {
          "id" :self.next_id,
          "title":book_data.title,
          "author" : book_data.author,

        }
                                     
     