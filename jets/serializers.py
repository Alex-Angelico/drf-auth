from rest_framework import serializers
from .models import Jets

class JetsSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id', 'name', 'engines', 'description', 'added_by', 'created_at', 'updated_at')
    model = Jets