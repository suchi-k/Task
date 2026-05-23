from django.urls import path, include
from .views import (BookAPIView, BookDetailsAPIView, 
                    AuthorAPIView, AuthorDetailsAPIView, 
                    RentalAPIView, RentalDetailsAPIView,
                    RentalAPIView, RentalDetailsAPIView, 
                    BookListByAuthor, ReturnBookAPI,
                    RentalOverDueAPI)
                    

urlpatterns = [
     # Basic CRUD API endpoints
     path('api/author', AuthorAPIView.as_view(), name='author_list_api_view'),   
     path('api/author_detail/<int:id>', AuthorDetailsAPIView.as_view(), name='author_detail_api_view'),

     path('api/book', BookAPIView.as_view(), name='book_list_api_view'),
     path('api/book_detail/<int:id>', BookDetailsAPIView.as_view(), name='book_detail_api_view'),
     
     path('api/rental', RentalAPIView.as_view(), name='rental_list_api_view'),   
     path('api/rental_detail/<int:id>', RentalDetailsAPIView.as_view(), name='rental_detail_api_view'),

     # Supporting API endpoints
     path('api/book_list', BookListByAuthor.as_view(), name='books_by_author'),
     path('api/book/return', ReturnBookAPI.as_view(), name='return_book'),
     path('api/rental/overdues', RentalOverDueAPI.as_view(), name='rental_overdue')
     
]