from rest_framework import generics, permissions

from . import models
from . import serializers

from .permissions import IsOwnerOrReadOnly

class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAuthenticated,
        IsOwnerOrReadOnly,)

