from django.contrib import admin
from django.urls import path ,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Task1.urls')),
    # path('user/', get_user, name='get_user'),
]
