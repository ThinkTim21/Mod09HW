import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test_case = BookLover("john doe","jon_doe@hotmail.com","fiction")
        test_case.add_book("War of the Worlds", 4)
        assert test_case.book_list.book_name.eq("War of the Worlds").any(), "error book not added"

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test_case = BookLover("john doe","jon_doe@hotmail.com","fiction")
        test_case.add_book("War of the Worlds", 4)
        test_case.add_book("War of the Worlds", 4)
        assert len(test_case.book_list.loc[test_case.book_list['book_name'] == "War of the Worlds"].book_name) == 1, "error book added twice"        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        test_case = BookLover("john doe","jon_doe@hotmail.com","fiction")
        test_case.add_book("War of the Worlds", 4)
        assert test_case.has_read("War of the Worlds"), "This method failed"
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        test_case = BookLover("john doe","jon_doe@hotmail.com","fiction")
        test_case.add_book("War of the Worlds", 4)
        self.assertFalse(test_case.has_read("A midsummers nights dream"), "This method failed")
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        test_case = BookLover("john doe","jon_doe@hotmail.com","fiction")
        test_case.add_book("War of the Worlds", 4)
        test_case.add_book("Tornado Alley", 5)
        test_case.add_book("War and Peace", 2)
        expected = 3
        assert test_case.num_books_read() == expected, "This method has failed"
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        test_case = BookLover("john doe","jon_doe@hotmail.com","fiction")
        test_case.add_book("War of the Worlds", 4)
        test_case.add_book("Tornado Alley", 5)
        test_case.add_book("War and Peace", 2)
        test_case.add_book("Italian for Dummies", 3)
        test_dataframe = test_case.fav_books()
        assert (test_dataframe.book_rating > 3).all(), "failed"
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
    