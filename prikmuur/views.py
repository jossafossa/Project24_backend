from django.shortcuts import render

from rest_framework import generics

from .models import Post
from .serializers import PrikmuurSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PrikmuurSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PrikmuurSerializer

