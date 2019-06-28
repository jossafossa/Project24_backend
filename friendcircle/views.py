from rest_framework import generics, permissions
from rest_framework.views import APIView
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

class GetMyMemberships(generics.ListAPIView):
    serializer_class = serializers.FriendCircleSerializer
    def get_queryset(self):
        return(models.FriendCircle.objects.filter(friendcirclemembership__user=self.request.user))

class GetMatchCandidateFriendCircle(generics.ListAPIView):
    serializer_class = serializers.FriendCircleSerializer
    def get_queryset(self):
        groups = models.FriendCircle.objects.all()

        # Exclude groups already swiped
        already_swiped_qs = models.FriendCircleMatcher.objects.filter(user=self.request.user)
        already_swiped_qs = already_swiped_qs.exclude(user_match_status='O')
        for already_swiped in already_swiped_qs:
            groups = groups.exclude(id=already_swiped.friendcircle.id)
        return(groups)

class SwipeCandidateFriendCircle(generics.CreateAPIView):
    serializer_class = serializers.SwipeCandidateFriendCircleSerializer
