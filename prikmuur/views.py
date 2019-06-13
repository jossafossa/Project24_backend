from django.shortcuts import render

from rest_framework import generics, permissions

from .models import Post
from .serializers import PrikmuurSerializer
from .permissions import IsOwnerOrReadOnly

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PrikmuurSerializer
    def perform_create(self, serializer):
        serializer.save(postedBy=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PrikmuurSerializer
    permission_classes = (permissions.IsAuthenticated,
        IsOwnerOrReadOnly,)
