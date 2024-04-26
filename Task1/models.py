from django.db import models
from django.import Book,Author,Rental


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author,on_delete =models.CASCADE)
    publication_year = models.IntegerField(max_length=10)

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()

class Rental(models.Model):
    book_Id = models.ForeignKey(Book,on_delete=models.CASCADE) 
    renter_name = models.CharField(max_length=100)
    rental_date = models.DateTimeField(max_length=100)
    return_Date = models.DateTimeField(max_length=100)

    
