import pandas as pd
class BookLover:
    
    def __init__(self,name, email,fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books =  num_books if book_list.book_name.nunique() == 0 else book_list.book_name.nunique()
        self.book_list = book_list
    def add_book(self,book_name, book_rating):
        if self.book_list.book_name.eq(book_name).any():
            print("This book is already in the list.")
        else:
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [book_rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
    def has_read(self, book_name):
        if self.book_list.book_name.eq(book_name).any():
            return True
        else:
            return False
    def num_books_read(self):
        return self.num_books
    def fav_books(self):
        self.fav_book_list = self.book_list.loc[self.book_list['book_rating'] > 3]
        return self.fav_book_list
