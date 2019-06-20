import random
from django.shortcuts import render

from rest_framework import generics, permissions

from django.contrib.auth.models import Group
from users.models import CustomUser
from users.serializers import UserSerializer

def pick_random_object(model):
    return random.randrange(1, model.objects.all().count() + 1)

class GetMatchCandidateGroup(generics.ListAPIView):
    #queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    def get_queryset(self):
        return CustomUser.objects.all().filter(id = pick_random_object(CustomUser))

#class GetMatchCandidateUser(generics.ListAPIView):
    
