from rest_framework import serializers
from api.models.accommodation import Accommodation
class AccommodationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accommodation
        fields = ['id', 'trip', 'name', 'tag', 'location', 'date', 'note', 'created_at']