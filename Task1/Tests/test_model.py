from django.test import TestCase
from Task1.models import *
class BookModelTest(TestCase):
    def test_create_Book(self):
        title = 'Test title'
        author = 'testauthor'
        publication_year= 'testpublication_year'

        Book = Book.objects.create_Book(title=title,author=author,
         publication_year= publication_year)
        
        self.assertEqual(Book.title,title)
        self.assertEqual(Book.author,author)
        self.assertTrue(Book.check_publication_year(publication_year))

class AuthorModelTest(TestCase):
    def test_create_Author(self):
        name = 'Testname'
        biography = 'Test biography'

        Author = Author.objects.create_Author(name=name,biography=biography)
        
        self.assertEqual(Author.name,name)
        self.assertEqual(Author.biography,biography)
        
class RentalModelTest(TestCase):
    def test_create_Rental(self):
        book_Id = 'Test book_id'
        renter_name = 'Test renter_name'
        rental_date = 'Test rental_date'
        return_Date = 'Test return_date'

        Rental = Rental.objects.create_Rental(book_Id = book_Id,
            renter_name=renter_name,rental_date=rental_date,return_Date=return_Date)                                      )

        self.assertEqual(Rental.book_id,book_Id)  
        self.assertEqual(Rental.renter_name,renter_name) 
        self.assertFalse(Rental.rental_date,rental_date)  
        self.assertEqual(Rental.return_Date,return_Date) 
 



