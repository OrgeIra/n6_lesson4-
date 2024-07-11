from django.contrib import admin
from .models import Author, Book
from import_export.admin import ImportExportModelAdmin

@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    list_display = ("id", "first_name", "last_name", "birth_date", "created_at")
    list_display_links = ("first_name", "last_name")
    search_fields = ("id", "first_name", "last_name")
    ordering=("first_name", "last_name", )


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ("id", "title", "author", "price", "created_at")
    list_display_links = ("title", "author")

