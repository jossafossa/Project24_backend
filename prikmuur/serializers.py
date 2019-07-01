from rest_framework import serializers
from .models import Post

class PrikmuurSerializer(serializers.ModelSerializer):
    postedBy = serializers.ReadOnlyField(source='postedBy.username')
    #group = serializers.ReadOnlyField(source='group.name')
    class Meta:
        model = Post
        # url terugzetten
        fields = ('url', 'id', 'subject', 'noticeText', 'postedBy', 'group', 'created', )
