from django.db import models

# Create your models here.
class Post(models.Model):
    from_someone = models.CharField(max_length=20, default='unknown')
    to_someone = models.CharField(max_length=20)
    message = models.CharField(max_length=120)

