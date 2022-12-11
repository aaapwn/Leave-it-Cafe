from django.contrib import admin
from .models import Message
# Register your models here.

class Messageadmin(admin.ModelAdmin):
    list_display = ['displayname', 'date', 'text']
    search_fields = ['displayname', 'text']

admin.site.register(Message, Messageadmin)
