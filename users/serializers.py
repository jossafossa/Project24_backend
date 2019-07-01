from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('url', 'id', 'email', 'username','interests', 'pic1', 'pic2', 'pic3', 'pic4', 'pic5', 'memberships'  )
