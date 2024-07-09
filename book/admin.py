from django.contrib import admin
from .models import Author, Book, Comment

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "birth_date", "created_at")
    list_display_links = ("first_name", "last_name")
    search_fields = ("id", "first_name", "last_name")
    ordering=("first_name", "last_name", )

admin.site.register(Book)
admin.site.register(Comment)
