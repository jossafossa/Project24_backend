from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    interests = models.ManyToManyField('interests.Interest', blank=True)
    pic1 = models.ImageField(blank=True)
    pic2 = models.ImageField(blank=True)
    pic3 = models.ImageField(blank=True)
    pic4 = models.ImageField(blank=True)
    pic5 = models.ImageField(blank=True)
    def __str__(self):
        return self.email

