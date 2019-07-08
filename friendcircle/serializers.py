from rest_framework import serializers
from rest_framework.utils import model_meta
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
    def create(self, validated_data):
        # Remove many-to-many relationships from validated_data.
        # They are not valid arguments to the default `.create()` method,
        # as they require that the instance has already been saved.
        ModelClass = self.Meta.model

        info = model_meta.get_field_info(ModelClass)
        many_to_many = {}
        for field_name, relation_info in info.relations.items():
            if relation_info.to_many and (field_name in validated_data):
                many_to_many[field_name] = validated_data.pop(field_name)
        for x in validated_data:
            print(x)
        # Voeg de aanmakende gebruiker toe aan de net aangemaakte groep
        instance = ModelClass._default_manager.create(**validated_data)
        instance.members.add(self.context['request'].user)

        # Save many-to-many relationships after the instance is created.
        if many_to_many:
            for field_name, value in many_to_many.items():
                field = getattr(instance, field_name)
                field.set(value)

        return instance

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

