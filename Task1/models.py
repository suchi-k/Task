from django.db import models


# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author,on_delete =models.CASCADE)
    publication_year = models.IntegerField()


class Rental(models.Model):
    book_Id = models.ForeignKey(Book,on_delete=models.CASCADE) 
    renter_name = models.CharField(max_length=100)
    rental_date = models.DateTimeField(max_length=100)
    return_Date = models.DateTimeField(max_length=100)

    
