from rest_framework import serializers
from .models import Book,Author,Rental

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Book
        fields = "__all__"

class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Author
        fields = "__all__"
class RentalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        fields = "__all__"    

