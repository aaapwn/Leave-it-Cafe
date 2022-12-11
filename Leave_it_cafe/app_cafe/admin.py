from django.contrib import admin
from .models import Message
# Register your models here.

class Messageadmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'text']
    search_fields = ['user', 'text']

admin.site.register(Message, Messageadmin)
