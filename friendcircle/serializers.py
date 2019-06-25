from rest_framework import serializers
from . import models

class FriendCircleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FriendCircle
        fields = ('url', 'id', 'name', 'description', 'interests',  )
