from django.db import models

# Create your models here.
class Post(models.Model):
    from_someone = models.CharField(max_length=20, default=False)
    to_someone = models.CharField(max_length=20, default=False)
    message = models.CharField(max_length=120)
