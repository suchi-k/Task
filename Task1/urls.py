from django.urls import path, include
from .views import (BookAPIView, BookDetailsAPIView,AuthorAPIView,AuthorDetailsAPIView,AuthorListView, RentalAPIView, RentalDetailsAPIView,
                    RentalAPIView,RentalDetailsAPIView)
                    
                    

urlpatterns = [
     # Normal Views
     # path('book/', book_list, name='book_list'),
     # path('author/', author_list, name='author_list'),
     # path('rental/', rental_list, name='rental_list'),

     path('api/book/', BookAPIView.as_view(),name='book_list_api_view'),
        
     path('api/detail/<int:id>/',BookDetailsAPIView.as_view(), name='book_detail_api_view'),
     path('api/author/', AuthorAPIView.as_view(),name='author_list_api_view'),
        
     path('api/detail/<int:id>/',AuthorDetailsAPIView.as_view(), name='author_detail_api_view'),
     path('api/rental/',RentalAPIView.as_view(),name='rental_list_api_view'),
        
     path('api/detail/<int:id>/',RentalDetailsAPIView.as_view(), name='rental_detail_api_view'),




]