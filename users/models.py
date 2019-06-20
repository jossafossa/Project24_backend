from django.contrib.auth.models import AbstractUser
from django.db import models
import interests.models

class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    interests = models.ManyToManyField(interests.models.Interest, blank=True)
    pic1 = models.ImageField(blank=True)
    pic2 = models.ImageField(blank=True)
    pic3 = models.ImageField(blank=True)
    pic4 = models.ImageField(blank=True)
    pic5 = models.ImageField(blank=True)

    def __str__(self):
        return self.email

class FriendCircle(models.Model):
    name = models.CharField(blank=True, max_length=255)
    description = models.CharField(blank=True, max_length=1000)
    interests = models.ManyToManyField(interests.models.Interest, blank=True)

    def __str__(self):
        return self.name

class FriendCircleMembership(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    friendcircle = models.ForeignKey(FriendCircle, on_delete=models.CASCADE)
    startdate = models.DateTimeField(auto_now_add=True)
    enddate = models.DateTimeField(blank=True)

    def __str__(self):
        return self.user.name + " member at " + self.friendcircle.name

    class Meta:
        unique_together = (('user', 'friendcircle'))

