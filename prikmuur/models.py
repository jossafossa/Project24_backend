from django.db import models
from django.contrib.auth.models import Group
from users.models import CustomUser

class Post(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  group = models.ForeignKey(Group, related_name='prikmuurpost', on_delete=models.CASCADE)
  postedBy = models.ForeignKey(CustomUser, related_name='prikmuurpost', on_delete=models.CASCADE)
  subject = models.CharField(max_length=45)
  text = models.TextField()

  class Meta:
    ordering = ('created',)

  def __str__(self):
    return self.text

