from rest_framework import serializers
from . import models

class FriendCircleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FriendCircle
        fields = ('url', 'id', 'name', 'description', 'interests', 'members', )

class FriendCircleMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FriendCircleMembership
        fields = ('url', 'id', 'user', 'friendcircle', 'startdate', 'enddate', )

class FriendCircleMatcherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FriendCircleMatcher
        fields = ('url', 'id', 'user', 'user_match_status', 'friendcircle', 'friendcircle_match_status', )

class SwipeCandidateFriendCircleSerializer(serializers.Serializer):
    friendcircle = serializers.PrimaryKeyRelatedField(queryset=models.FriendCircle.objects.all())
    swipe_choice = serializers.ChoiceField(choices=['V', 'X',],)
    def save(self):
        friendcircle = self.validated_data['friendcircle']
        swipe_choice = self.validated_data['swipe_choice']
        obj, created = models.FriendCircleMatcher.objects.get_or_create(user=self.context['request'].user, friendcircle=friendcircle)
        # Only allow status to be set when no choice has yet been made.
        if obj.user_match_status == 'O':
            obj.user_match_status = swipe_choice
            obj.save()
