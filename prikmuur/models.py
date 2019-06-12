from django.db import models
from django.contrib.auth.models import Group
from users.models import CustomUser

class Post(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  group = models.ForeignKey(Group, on_delete=models.CASCADE)
  postedBy = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  text = models.TextField()

  class Meta:
    ordering = ('created',)

