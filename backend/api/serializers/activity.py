from rest_framework import serializers
from api.models.activity import Activity

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'trip', 'name', 'location', 'activity_time', 'note', 'created_at']