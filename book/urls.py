from django.urls import path
from .views import book, home, search, author

urlpatterns = [
    path('', home, name='home'),
    path('book/', book, name='book'),
    path('search/', search, name='search'), 
    path('author/', author, name='author')
]

