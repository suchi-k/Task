from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (Book,Author,Rental)

class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Book
        fields = ('id', 'name', )

class AuthorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'gender', 'age', )

class RentalSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

