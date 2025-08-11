from rest_framework import serializers
from api.models.place import Place

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'trip', 'name', 'tag', 'itinerary_day', 'note', 'created_at']