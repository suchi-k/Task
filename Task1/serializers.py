from rest_framework import serializers
from .models import Book,Author,Rental


class AuthorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Book
        fields = "__all__"


class RentalSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    # book = BookSerializer()

    class Meta:
        model = Rental
        # fields = ('book', 'renter_name', 'rental_date', 'return_Date',)
        fields = "__all__"

