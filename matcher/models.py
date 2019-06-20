from django.db import models

from users.models import CustomUser, FriendCircle

MATCH_STATUS = (
    ('O', 'Not swiped',),
    ('V', 'Swiped Right',),
    ('X', 'Swiped Left',),
)

# Keeps track of matches. If both parties swiped right, the user can be added to the friendcircle
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
        return self.user.name + " + " + self.friendcircle.name

    class Meta:
        unique_together = (('user', 'friendcircle'))

