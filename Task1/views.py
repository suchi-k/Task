from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import action, api_view
from .models import Book, Author, Rental
from .serializers import BookSerializer, AuthorSerializer, RentalSerializer
from django.shortcuts import get_object_or_404

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
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Rental Object created successfully", 
                             "data":serializer.data
                             }, 
                             status=status.HTTP_201_CREATED)
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
# --------DRF Class Based Views | APIView --------        

