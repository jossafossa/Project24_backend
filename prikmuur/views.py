from django.shortcuts import render, get_object_or_404
from rest_framework import generics, permissions

from .models import Post
from .serializers import PrikmuurSerializer
from .permissions import IsOwnerOrReadOnly

class PostList(generics.ListCreateAPIView):
    serializer_class = PrikmuurSerializer
#    queryset = Post.objects.all()

#    def perform_create(self, serializer):
#        serializer.save(postedBy=self.request.user, group=self.kwargs.get('fcpk'))

    def get_queryset(self):
        friendcircle = self.kwargs.get('pk')
        if friendcircle:
            return Post.objects.filter(group=friendcircle)
        else:
            return Post.objects.all()


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PrikmuurSerializer
    permission_classes = (permissions.IsAuthenticated,
        IsOwnerOrReadOnly,)
