from django.db import models
from datetime import datetime
from app_home.models import Profile
# Create your models here.

class Message(models.Model):
    text = models.CharField(max_length=120)
    date = models.DateTimeField(default=datetime.now, blank=True)
    displayname = models.CharField(max_length=20)
