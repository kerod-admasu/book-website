# file: appName/admin.py

from django.contrib import admin
from book.models import * # import the tables

# Register your models here.

admin.site.register(Product)

