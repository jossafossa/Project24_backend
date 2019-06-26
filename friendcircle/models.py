from django.db import models
import interests.models
from users.models import CustomUser

class FriendCircle(models.Model):
    name = models.CharField(blank=True, max_length=255)
    description = models.CharField(blank=True, max_length=1000)
    interests = models.ManyToManyField(interests.models.Interest, blank=True)

    def __str__(self):
        return self.name


# Keeps track of FriendCircle memberships
class FriendCircleMembership(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    friendcircle = models.ForeignKey(FriendCircle, on_delete=models.CASCADE)
    startdate = models.DateTimeField(auto_now_add=True)
    enddate = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.name + " member at " + self.friendcircle.name

    class Meta:
        unique_together = (('user', 'friendcircle'))


MATCH_STATUS = (
    ('O', 'Not swiped',),
    ('V', 'Swiped Right',),
    ('X', 'Swiped Left',),
)

# Keeps track of matches. If both parties swiped right, the user can be added to FriendCircleMembership
class FriendCircleMatcher(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    user_match_status = models.CharField(max_length=1,
                     choices=MATCH_STATUS,
                     default="O")
    friendcircle = models.ForeignKey(FriendCircle, on_delete=models.CASCADE)
    friendcircle_match_status = models.CharField(max_length=1,
                     choices=MATCH_STATUS,
                     default="O")
    def __str__(self):
        return self.user.email + " + " + self.friendcircle.name

    class Meta:
        unique_together = (('user', 'friendcircle'))

