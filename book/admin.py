from django.contrib import admin
from .models import Author, Book, Comment

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'image')

admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(Comment)
