from django.urls import path
from .views import book_list


urlpatterns = [
     path('book/', book_list, name='book_list'),
]