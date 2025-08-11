from rest_framework import serializers
from api.models.outfit import Outfit

class OutfitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outfit
        fields = ['id', 'trip', 'day', 'outfit_name', 'note', 'created_at']
