from django.urls import path
from .views import book, home

urlpatterns = [
    path('', home, name='home'),
    path('book/', book, name='book')
]
