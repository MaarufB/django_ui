from django.contrib import admin
from .models import (Movie, Blog, Book, Author)
# Register your models here.

admin.site.register([Movie, Blog, Book, Author])