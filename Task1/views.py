from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import action, api_view
from .models import Book, Author, Rental
from .serializers import BookSerializer, AuthorSerializer, RentalSerializer
from django.shortcuts import get_object_or_404
from django.db.models import ExpressionWrapper, F, DurationField
from rest_framework import generics
from datetime import datetime, timedelta
from django.http import JsonResponse, HttpResponseNotFound

from rest_framework.authentication import (BasicAuthentication, TokenAuthentication,
                                           SessionAuthentication)
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
# --------DRF Class Based Views | APIView --------
class BookAPIView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Book Object created successfully",
                             "data":serializer.data
                             }, 
                             status=status.HTTP_201_CREATED)
        else:
            return Response({"message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class BookDetailsAPIView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            book = Book.objects.get(id=id)
            serializer = BookSerializer(book)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({"message":f"Article object for id {id} is Not Found"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        book = Book.objects.get(id=id)
        serializer = BookSerializer(book, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Book Object Updated successfully",
                            "data":serializer.data
                            }, 
                            status=status.HTTP_200_OK)

        return Response({"message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        book = Book.objects.get(id=id)
        book.delete()
        return Response({"message", f"Book object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class AuthorAPIView(APIView):
    # authentication_classes = [SessionAuthentication, TokenAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Author object created Successfully",
                            "data":serializer.data
                             }, 
                            status=status.HTTP_201_CREATED)
        else:
            return Response({"message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetailsAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            author = Author.objects.get(id=id)
            serializer = AuthorSerializer(author)
            return Response({"data":serializer.data}, status=status.HTTP_200_OK)
        except Author.DoesNotExist:
            return Response({"message": f"Author object for id {id} is Not Found"}, status=status.HTTP_404_NOT_FOUND)
    
    
    def put(self, request, id):
        author = Author.objects.get(id=id)
        serializer = AuthorSerializer(author, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Author Object Updated successfully",
                            "data":serializer.data
                             }, 
                             status=status.HTTP_200_OK)

        return Response({"message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        author = Author.objects.get(id=id)
        author.delete()
        return Response({"message", f"Author object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class RentalAPIView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        rentals = Rental.objects.all()
        serializer = RentalSerializer(rentals, many=True)
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RentalSerializer(data=request.data)
        data = request.data
        book_id = data["book"]
        if serializer.is_valid():
            book = Book.objects.get(id =book_id)
            if not book.is_rented:
                serializer.save()
                return Response({"message":"Rental Object created successfully", 
                             "data":serializer.data
                             }, 
                             status=status.HTTP_201_CREATED)
            else:
                return Response({"message":"The book is not availble for rented"},status=status.HTTP_200_OK)
        else:
            return Response({"message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class RentalDetailsAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
        
    def get(self, request, id):
        try:
            rental = Rental.objects.get(id=id)
            serializer = RentalSerializer(rental)
            return Response({"data":serializer.data}, status=status.HTTP_200_OK)
        except Rental.DoesNotExist:
            return Response({"message": f"Rental object for id {id} is Not Found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        rental = Rental.objects.get(id=id)
        serializer = RentalSerializer(rental, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Rental Object Updated successfully",
                            "data":serializer.data
                             }, 
                            status=status.HTTP_200_OK)

        return Response({"message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        rental = Rental.objects.get(id=id)
        rental.delete()
        return Response({"message", f"Rental object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class BookListByAuthor(generics.ListAPIView):
    """ 
    We are using Django Filters to filter the Book written by Authors and as well as Rented
    In a similar way we can implement Search Filter to filter the objects in a given resource/Table
    """
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'is_rented']
    queryset = Book.objects.all()

    # def get_queryset(self):
    #     """ Override method """
    #     queryset = Book.objects.all()
    #     author = self.request.query_params.get('author')
    #     if author is not None:
    #         queryset = queryset.filter(author__name=author)
    #     return queryset


class ReturnBookAPI(APIView):
    """ Need to Return the Book which is rented.
     
     We can get the following details from Request body 
     request: {
        "rental_id":int,
        "book_id":int,
        "return_date":"YYYY-mm-dd"
        }  
     
     Now we can update the rental record with the return date
     also we update Book is_rented field as False from True
    """
    def put(self, request):
        try:
            data = request.data
            rental_id, book_id, return_date = data['rental_id'], data['book_id'], data['return_date']
            
            # marking the return_date for Rental object
            rental = Rental.objects.get(id=rental_id)
            rental.return_date = datetime.strptime(return_date, "%Y-%m-%d")
            rental.save()

            # Marking Book Model is_rented field as False so that the book is available for rent.
            book = Book.objects.get(id=book_id)
            book.is_rented = False
            book.save()

            return Response({"message":"Rental Object Updated successfully"},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)


class RentalOverDueAPI(APIView):
    def get(self, request):
        # Calculate the date 14 days ago from the current date
        current_date = datetime.now()
        overdue_date = current_date - timedelta(days=14)

        try:
            rentals = Rental.objects.filter(rental_date__lte=overdue_date, return_date__isnull=True)
            serializer = RentalSerializer(rentals, many=True)
            if serializer.data:
                return Response({"overdue_rentals":serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"message":"No Overdue Rentals found"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
# --------DRF Class Based Views | APIView --------        

