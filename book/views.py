from django.shortcuts import render
from .models import Book, Author

def home(request):
    return render(request, 'home.html')

def book(request):
    books = Book.objects.all()  
    return render(request, 'book.html', {'books': books})


def search(request):
    query = request.GET.get('q')
    if query:
        results = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__first_name__icontains=query)
    else:
        results = Book.objects.all()  # If the query is empty, return all books
    
    return render(request, 'search_results.html', {'results': results, 'query': query})

def author(request):
    authors = Author.objects.all()  # Retrieve all authors from the database
    return render(request, 'author.html', {'authors': authors})

