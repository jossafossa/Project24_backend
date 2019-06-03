from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

class Post(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  group = models.ForeignKey(Group, on_delete=models.CASCADE)
  postedBy = models.ForeignKey(User, on_delete=models.CASCADE)
  text = models.TextField()

  class Meta:
    ordering = ('created',)
