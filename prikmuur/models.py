from django.db import models
from django.contrib.auth.models import Group
from users.models import CustomUser
from friendcircle.models import FriendCircle

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(FriendCircle, related_name='prikmuurpost', on_delete=models.CASCADE)
    postedBy = models.ForeignKey(CustomUser, related_name='prikmuurpost', on_delete=models.CASCADE)
    subject = models.CharField(max_length=45)
    noticeText = models.TextField()

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.subject
