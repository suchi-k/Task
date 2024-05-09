from django.test import TestCase
from datetime import datetime
from Task1.models import Author, Book, Rental
from django.urls import reverse
import json

class ModelTestCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="suchi", biography="I am writer")
        self.book = Book.objects.create(title="Python Concepts", author=self.author, publication_year=2024)
        self.rental = Rental.objects.create(book_Id=self.book, renter_name="suki", rental_date=datetime.now(), return_Date=datetime.now())

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
        """ Test rental Creation """
        rental = Rental.objects.get(id=self.rental.id)
        self.assertTrue(isinstance(rental, Rental))
        self.assertEqual(rental.renter_name, 'suki')
        print('Test Rental Creation --- OK')


class TestURLs(TestCase):
    def test_author_url(self):
        url = reverse('author_list_api_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        print('Test author_list_api_view -- OK')

    def test_author_detail_url(self):
        url = reverse('author_detail_api_view', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        print('Test author_detail_api_view -- OK')