from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
import random

from . import models
from . import serializers
from users.serializers import UserSerializer
from users.models import CustomUser

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
        groups = models.FriendCircle.objects.filter(friendcirclemembership__user=self.request.user)

        # Exclude groups already swiped
        already_swiped_qs = models.FriendCircleMatcher.objects.filter(user=self.request.user)
        already_swiped_qs = already_swiped_qs.exclude(user_match_status='O')
        for already_swiped in already_swiped_qs:
            groups = groups.exclude(id=already_swiped.friendcircle.id)
        return(groups)

class GetMatchCandidateUser(generics.ListAPIView):
    serializer_class = UserSerializer
    def get_queryset(self):
        friendcircle = self.kwargs.get('pk')
        users = CustomUser.objects.all()

        # Exclude groups already swiped
        already_swiped_qs = models.FriendCircleMatcher.objects.filter(friendcircle_id=friendcircle)
        already_swiped_qs = already_swiped_qs.exclude(friendcircle_match_status='O')
        for already_swiped in already_swiped_qs:
            users = users.exclude(id=already_swiped.user.id)

        return(users)


class SwipeCandidateFriendCircle(generics.CreateAPIView):
    serializer_class = serializers.SwipeCandidateFriendCircleSerializer

class SwipeCandidateUser(APIView):
    serializer_class = serializers.SwipeCandidateUserSerializer
    def post(self, request, pk, format=None):

        try:
            friendcircle = models.FriendCircle.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

        serializer = serializers.SwipeCandidateUserSerializer(data=request.data,  context={'friendcircle': friendcircle})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

