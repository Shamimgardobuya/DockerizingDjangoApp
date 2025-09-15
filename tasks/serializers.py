from rest_framework import serializers
from .models import Tasks

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields =(
                    'title', 'description', 'reminder_time', 'image', 'new_priority'
                )
        
        
        def validate_name(self, value):
            if len(value) < 5:
                raise serializers.ValidationError("Name must be at least 5 characters long.")
            return value