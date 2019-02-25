from django.contrib import admin

# Register your models here.
from catalog.models import Author, Genre, Book, Language, BookInstance

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)

