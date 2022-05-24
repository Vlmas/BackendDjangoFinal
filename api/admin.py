from django.contrib import admin
from api.models import *


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'description', 'created_at', 'num_pages', 'genre']


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'description', 'created_at', 'type', 'publisher']
