from django.test import TestCase
from datetime import datetime
from Task1.models import Author, Book, Rental
from django.urls import reverse
import json
from django.contrib.auth.models import User

class ModelTestCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="suchi", biography="I am writer")
        self.book = Book.objects.create(title="Python Concepts", author=self.author, publication_year=2024)
        self.rental = Rental.objects.create(book_Id=self.book, renter_name="suki", 
                                            rental_date=datetime.strptime('2024-04-29', '%Y-%m-%d'),
                                            return_Date=datetime.strptime('2024-05-01', '%Y-%m-%d'))

    def test_author_creation(self):
        """ Test Author Creation """
        author = Author.objects.get(id=self.author.id)
        self.assertTrue(isinstance(author, Author))
        self.assertEqual(author.name, 'suchi')
        print('Test Author Creation --- OK')
    
    def test_book_creation(self):
        """ Test Book Creation """
        book = Book.objects.get(id=self.book.id)
        self.assertTrue(isinstance(book, Book))
        self.assertEqual(book.title, 'Python Concepts')
        print('Test Book Creation --- OK')

    def test_rental_creation(self):
        """ Test Rental Creation """
        rental = Rental.objects.get(id=self.rental.id)
        self.assertTrue(isinstance(rental, Rental))
        self.assertEqual(rental.renter_name, 'suki')
        print('Test Rental Creation --- OK')


class TestURLs(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()

        self.author = Author.objects.create(name="suchi", biography="I am writer")
        self.book = Book.objects.create(title="Python Concepts", author=self.author, publication_year=2024)
        self.rental = Rental.objects.create(book_Id=self.book, renter_name="suki", 
                                            rental_date=datetime.strptime('2024-04-29', '%Y-%m-%d'),
                                            return_Date=datetime.strptime('2024-05-01', '%Y-%m-%d'))
        
    def test_author_url(self):
        url = reverse('author_list_api_view')
        self.client.login(username=self.user.username, password='12345')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        print('Test author_list_api_view -- OK')

    def test_author_detail_url(self):
        url = reverse('author_detail_api_view', args=[1])
        self.assertEqual(url, '/api/author_detail/1')
        self.client.login(username=self.user.username, password='12345')
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        output = {'id': 1, 'name': 'suchi', 'biography': 'I am writer'}
        self.assertTrue(isinstance(response.json()["data"], dict))
        self.assertEqual(response.json()["data"], output)
        
        print('Test author_detail_api_view -- OK')

    def test_book_url(self):
        url = reverse('book_list_api_view')
        self.client.login(username=self.user.username, password='12345')
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        print('Test book_list_api_view -- OK')


    def test_book_detail_url(self):
        url = reverse('book_detail_api_view', args=[1])
        self.assertEqual(url, '/api/book_detail/1')
        self.client.login(username=self.user.username, password='12345')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        output = {'id': 1, 'title': "Python Concepts", 'author': 1,'publication_year':2024}
        self.assertTrue(isinstance(response.json()["data"], dict))
        self.assertEqual(response.json()["data"], output)
        
        print('Test book_detail_api_view -- OK')

    def test_rental_url(self):
        url = reverse('rental_list_api_view')
        self.client.login(username=self.user.username, password='12345')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        print('Test rental_list_api_view -- OK')


    def test_rental_detail_url(self):
        url = reverse('rental_detail_api_view', args=[1])
        self.assertEqual(url, '/api/rental_detail/1')
        self.client.login(username=self.user.username, password='12345')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
        output = {'id': 1, 'renter_name':'suki', 
                  'rental_date':'2024-04-29T00:00:00Z', 
                  'return_Date':'2024-05-01T00:00:00Z',
                  'book_Id':1}
        self.assertTrue(isinstance(response.json()["data"], dict))
        self.assertEqual(response.json()["data"], output)
        
        print('Test rental_detail_api_view -- OK')
        


# class ViewTestCase(TestCase):
#     def setUp(self):
#         self.author = Author.objects.create(name="suchi", biography="I am writer")
#         self.book = Book.objects.create(title="Python Concepts", author=self.author, publication_year=2024)
#         self.rental = Rental.objects.create(book_Id=self.book, renter_name="suki", 
#                                             rental_date=datetime.strptime('2024-04-29', '%Y-%m-%d'),
#                                             return_Date=datetime.strptime('2024-05-01', '%Y-%m-%d'))


#     def test_book_my_view(self):
#         url = reverse('book_list_api_view')  # Assuming 'my_view' is the name of your URL pattern
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.content.decode(), "Hello, world!")

#     def test_author_my_view(self):
#         url = reverse('author_list_api_view')  # Assuming 'my_view' is the name of your URL pattern
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.content.decode(), "Hello, world!")

#     def test_rental_my_view(self):
#         url = reverse('rental_list_api_view')  # Assuming 'my_view' is the name of your URL pattern
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.content.decode(), "Hello, world!")

