from rest_framework import serializers
from .models import PrikmuurPost

class PrikmuurSerializer(serializers.ModelSerializer):
  class Meta:
    model = PrikmuurPost
    fields = ('id', 'text', 'group', 'postedBy')
