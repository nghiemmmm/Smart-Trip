from rest_framework import serializers
from api.models.packing_list import PackingList

class PackingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackingList
        fields = ['id', 'trip', 'item_name', 'checked', 'created_at']