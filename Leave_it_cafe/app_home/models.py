from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class CustomUSer(AbstractUser):
    email = models.EmailField(unique=True)

class Profile(models.Model):
    displayname = models.CharField(max_length=20, default="Unknown")
    picture = models.CharField(max_length=100, default="app_home/image/profile_image.jfif")
    user = models.OneToOneField(CustomUSer, on_delete=models.CASCADE)
