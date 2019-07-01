from rest_framework import serializers
from . import models
from users.models import CustomUser
from interests.models import Interest

class FriendCircleSerializer(serializers.ModelSerializer):
    interests = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        slug_field='name',
        queryset=Interest.objects.all(),
     )
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
            # Add user to friendcircle when both swiped right
            if obj.user_match_status == 'V' and obj.friendcircle_match_status == 'V':
                member_obj, member_created = models.FriendCircleMembership.objects.get_or_create(user=self.context['request'].user, friendcircle=friendcircle)
                member_obj.save()

class SwipeCandidateUserSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    swipe_choice = serializers.ChoiceField(choices=['V', 'X',],)
    def save(self):
        user = self.validated_data['user']
        swipe_choice = self.validated_data['swipe_choice']
        friendcircle = self.context.get('friendcircle')
        obj, created = models.FriendCircleMatcher.objects.get_or_create(user=user, friendcircle=friendcircle)
        # Only allow status to be set when no choice has yet been made.
        if obj.friendcircle_match_status == 'O':
            obj.friendcircle_match_status = swipe_choice
            obj.save()
            # Add user to friendcircle when both swiped right
            if obj.user_match_status == 'V' and obj.friendcircle_match_status == 'V':
                member_obj, member_created = models.FriendCircleMembership.objects.get_or_create(user=user, friendcircle=friendcircle)
                member_obj.save()

