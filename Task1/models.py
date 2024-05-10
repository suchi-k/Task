from django.db import models

from datetime import datetime, timedelta
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete =models.CASCADE)
    is_rented = models.BooleanField(default=False)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title


class Rental(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE) 
    renter_name = models.CharField(max_length=100)
    rental_date = models.DateTimeField()
    return_date = models.DateTimeField(blank=True, null=True)
  
    def __str__(self):
        return self.book.title
    
    def save(self, *args, **kwargs):
        # Set the Book model is_rented field as True 
        # and save the Book Model before saving the Rental model.
        self.book.is_rented = True
        self.book.save()
        
        # Call the parent save method.
        super(Rental, self).save(*args, **kwargs)





       




    

    
