from rest_framework import serializers
from api.models import UserProfile



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')