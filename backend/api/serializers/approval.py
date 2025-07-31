from rest_framework import serializers
from api.models import Approval


class ApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Approval
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')