from django.contrib import admin

from qapp.models import Author, Blog, Entry

# Register your models here.

admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
