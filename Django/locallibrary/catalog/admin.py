from django.contrib import admin

# Register your models here.

from catalog.models import Author, Genre, Book, BookInstance

admin.site.register(Book)
admin.site.register(Author)
admin.site.registeR(Genre)
admin.site.register(BookInstance)
