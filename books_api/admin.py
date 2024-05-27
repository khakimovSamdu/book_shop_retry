from django.contrib import admin
from .models import Auther, Genre, Books

# Register your models here.

admin.site.register(Auther)
admin.site.register(Genre)
admin.site.register(Books)