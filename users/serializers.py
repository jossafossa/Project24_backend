from rest_framework import serializers
from . import models
from interests.models import Interest

class UserSerializer(serializers.ModelSerializer):
    interests = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        slug_field='name',
        queryset=Interest.objects.all(),
     )
    class Meta:
        model = models.CustomUser
        fields = ('url', 'id', 'email', 'username','interests', 'pic1', 'pic2', 'pic3', 'pic4', 'pic5', 'memberships'  )
