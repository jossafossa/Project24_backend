from rest_framework import serializers
from prikmuur.models import Post

class PrikmuurSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ('id', 'text', 'group', 'postedBy')
