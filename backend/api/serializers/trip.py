from rest_framework import serializers
from api.models.trip import Trip

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id', 'user', 'name', 'status', 'start_date', 'end_date', 'trip_type', 'created_at']