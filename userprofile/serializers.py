from django.contrib.auth.models import User, Group
from .models import Profile
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

#class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
#    user = serializers.HyperlinkedRelatedField(
#        view_name="user",
#        many=False,
#    )

#    class Meta:
#        model = Profile
#        fields = ('user')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
