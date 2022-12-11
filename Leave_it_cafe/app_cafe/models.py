from django.db import models
from datetime import datetime

# Create your models here.

class Message(models.Model):
    text = models.CharField(max_length=120)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=20)
