from rest_framework import generics, permissions
import random

from . import models
from . import serializers

class FriendCircleListView(generics.ListCreateAPIView):
    queryset = models.FriendCircle.objects.all()
    serializer_class = serializers.FriendCircleSerializer

class FriendCircleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.FriendCircle.objects.all()
    serializer_class = serializers.FriendCircleSerializer
    #permission_classes = (permissions.IsAuthenticated,
    #    IsOwnerOrReadOnly,)


def pick_random_from_qs(qs):
    return random.randrange(1, len(qs) + 1)

class GetMatchCandidateFriendCircle(generics.ListAPIView):
#    queryset = models.FriendCircle.objects.all()
    serializer_class = serializers.FriendCircleSerializer
    def get_queryset(self):
        groups = models.FriendCircle.objects.all()

        already_swiped_qs = models.FriendCircleMatcher.objects.filter(user=self.request.user)
        # Exclude groups already swiped
        for already_swiped in already_swiped_qs:
            if (already_swiped.user_match_status == 'O'):
                groups = groups.exclude(id=already_swiped.friendcircle.id)
        # Exclude groups that the user is already a member of
        
        groups = groups.filter(id = pick_random_from_qs(groups))
        return(groups)
