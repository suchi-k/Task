from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action, api_view
from .models import Book,Author,Rental
from .serializers import BookSerializer,AuthorSerializer,RentalSerializer
from django.shortcuts import get_object_or_404

from rest_framework.authentication import (BasicAuthentication, TokenAuthentication,
                                           SessionAuthentication)
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class BookAPIView(APIView):
    authentication_classes = [SessionAuthentication,
                              TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)


class BookDetailsAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response({"message": f"Article object for id {id} is Not Found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        book = self.get_object(id)

        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        book = Book.objects.get(id=id)
        serializer = BookSerializer(book, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        book = self.get_object(id)
        book.delete()
        return Response({"message", f"{book.title} object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
# --------DRF Class Based Views | APIView --------


class AuthorAPIView(APIView):
    authentication_classes = [SessionAuthentication,
                              TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        authors = Book.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)


class AuthorDetailsAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response({"message": f"Article object for id {id} is Not Found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        author = self.get_object(id)

        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        author = Book.objects.get(id=id)
        serializer = BookSerializer(author, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        author = self.get_object(id)
        author.delete()
        return Response({"message", f"{author.title} object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
# --------DRF Class Based Views | APIView --------

class RentalAPIView(APIView):
    authentication_classes = [SessionAuthentication,
                              TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        rentals = Rental.objects.all()
        serializer = RentalSerializer(rentals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RentalSerializer(data=request.data)


class RentalDetailsAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Rental.objects.get(id=id)
        except Rental.DoesNotExist:
            return Response({"message": f"Rental object for id {id} is Not Found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        rental = self.get_object(id)

        serializer = RentalSerializer(rental)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        rental = Rental.objects.get(id=id)
        serializer =RentalSerializer(rental, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        rental = self.get_object(id)
        rental.delete()
        return Response({"message", f"{rental.title} object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
# --------DRF Class Based Views | APIView --------        


#Bussiness logic

from datetime import datetime, timedelta

class Library:
    def __init__(self):
        self.books = {}
        self.rentals = {}

    def add_book(self, book_id, title):
        self.books[book_id] = title

    def rent_book(self, book_id, user_id):
        if book_id in self.rentals:
            print("This book is already rented.")
            return
        self.rentals[book_id] = {'user_id': user_id, 'rental_date': datetime.now()}

    def return_book(self, book_id):
        if book_id not in self.rentals:
            print("This book is not currently rented.")
            return
        del self.rentals[book_id]

    def check_overdue_rentals(self, max_rental_period_days=14):
        today = datetime.now()
        overdue_books = []
        for book_id, info in self.rentals.items():
            rental_date = info['rental_date']
            if today - rental_date > timedelta(days=max_rental_period_days):
                overdue_books.append((book_id, info['user_id'], rental_date))
        return overdue_books

# Example usage
library = Library()
library.add_book(1, "Book 1")
library.add_book(2, "Book 2")

library.rent_book(1, "User 1")
library.rent_book(2, "User 2")

# Trying to rent Book 1 again (already rented)
library.rent_book(1, "User 2")

# Returning Book 1
library.return_book(1)

# Checking for overdue rentals
overdue_books = library.check_overdue_rentals()
if overdue_books:
    print("Overdue rentals:")
    for book_id, user_id, rental_date in overdue_books:
        print(f"Book ID: {book_id}, User ID: {user_id}, Rental Date: {rental_date}")
else:
    print("No overdue rentals.")

# Testing

import unittest
from datetime import datetime, timedelta
from library import Library  # Assuming library.py contains the Library class implementation


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.library.add_book(1, "Book 1")
        self.library.add_book(2, "Book 2")

    def test_rent_book(self):
        self.library.rent_book(1, "User 1")
        self.assertIn(1, self.library.rentals)

    def test_return_book(self):
        self.library.rent_book(1, "User 1")
        self.library.return_book(1)
        self.assertNotIn(1, self.library.rentals)

    def test_overdue_rentals(self):
        today = datetime.now()
        rental_date = today - timedelta(days=15)  # Set rental date 15 days ago
        self.library.rentals = {1: {'user_id': "User 1", 'rental_date': rental_date}}
        overdue_books = self.library.check_overdue_rentals(max_rental_period_days=14)
        self.assertEqual(len(overdue_books), 1)
        self.assertEqual(overdue_books[0][0], 1)


if __name__ == '__main__':
    unittest.main()

# Error Handling and Validation    

from datetime import datetime, timedelta

class Library:
    def __init__(self):
        self.books = {}
        self.rentals = {}

    def add_book(self, book_id, title):
        if book_id in self.books:
            raise ValueError("Book with the same ID already exists.")
        self.books[book_id] = title

    def rent_book(self, book_id, user_id):
        if book_id not in self.books:
            raise ValueError("Book with the given ID does not exist.")
        if book_id in self.rentals:
            raise ValueError("This book is already rented.")
        self.rentals[book_id] = {'user_id': user_id, 'rental_date': datetime.now()}

    def return_book(self, book_id):
        if book_id not in self.books:
            raise ValueError("Book with the given ID does not exist.")
        if book_id not in self.rentals:
            raise ValueError("This book is not currently rented.")
        del self.rentals[book_id]

    def check_overdue_rentals(self, max_rental_period_days=14):
        today = datetime.now()
        overdue_books = []
        for book_id, info in self.rentals.items():
            rental_date = info['rental_date']
            if today - rental_date > timedelta(days=max_rental_period_days):
                overdue_books.append((book_id, info['user_id'], rental_date))
        return overdue_books

