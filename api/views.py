from django.shortcuts import render
from rest_framework import generics

from .models import PrikmuurPost
from .serializers import PrikmuurSerializer

class PostList(generics.ListCreateAPIView):
    queryset = PrikmuurPost.objects.all()
    serializer_class = PrikmuurSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PrikmuurPost.objects.all()
    serializer_class = PrikmuurSerializer
