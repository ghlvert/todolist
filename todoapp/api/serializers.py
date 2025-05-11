
from rest_framework import serializers

from todoapp.models import Task

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Task
        fields = ['id', 'title', 'text', 'state', 'created', 'updated', 'user']

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
    # def create(self, validated_data):
    #     user = self.context['request'].user
    #     validated_data['user'] = user
    #     return super().create(validated_data)