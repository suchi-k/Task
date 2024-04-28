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

