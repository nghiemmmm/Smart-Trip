from rest_framework import serializers
from api.models.itinerary import Itinerary

class ItinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Itinerary
        fields = ['id', 'trip', 'day_number', 'activity', 'time', 'created_at']