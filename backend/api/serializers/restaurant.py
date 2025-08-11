from rest_framework import serializers
from api.models.restaurant import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'trip', 'name', 'tag', 'location', 'itinerary_day', 'note', 'created_at']