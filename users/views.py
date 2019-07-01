from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404

from . import models
from . import serializers

from .permissions import IsOwnerOrReadOnly

def pick_random_from_qs(qs):
    return random.randrange(0, len(qs))

class GetMatchCandidateUser(generics.ListAPIView):
    #queryset = CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
    def get_queryset(self):
        users = models.CustomUser.objects.all()

        # Get all groups that this user has already swiped
        already_swiped_qs = models.FriendCircleMatcher.objects.all().filter(user=self.request.user)
        for already_swiped in already_swiped_qs:
            already_swiped_list.add(object.friendcircle)
        #print(already_swiped_groups)
        #user = CustomUser.objects.all().filter(id = pick_random_object(CustomUser))
        #print(user)
        return users

class GetMyUser(generics.RetrieveAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.request.user.id)
        return obj

class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAuthenticated,
        IsOwnerOrReadOnly,)

