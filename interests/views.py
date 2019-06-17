from django.shortcuts import render
from rest_framework import generics, permissions

from .models import Interest
from .serializers import InterestSerializer

class InterestList(generics.ListCreateAPIView):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
