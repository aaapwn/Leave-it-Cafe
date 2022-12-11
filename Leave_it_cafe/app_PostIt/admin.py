from django.contrib import admin
from .models import Post

# Register your models here.

class Postadmin(admin.ModelAdmin):
    list_display = ['id', 'to_someone', 'from_someone', 'message']
    search_fields = ['to_someone', 'from_someone']

admin.site.register(Post, Postadmin)
