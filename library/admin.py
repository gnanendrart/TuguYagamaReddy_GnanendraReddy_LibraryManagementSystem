from django.contrib import admin
from .models import Author, Book, Publisher, Section, Genre, Member

# Register your models here.

admin.site.register(Book)
admin.site.register(Member)
admin.site.register(Section)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Genre)