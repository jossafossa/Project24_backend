from rest_framework import serializers
from .models import Post

class PrikmuurSerializer(serializers.ModelSerializer):
  postedBy = serializers.ReadOnlyField(source='postedBy.username')
  class Meta:
    model = Post
    fields = ('id', 'text', 'group', 'postedBy')
