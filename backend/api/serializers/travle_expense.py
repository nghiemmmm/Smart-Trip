from rest_framework import serializers
from api.models.travel_expense import TravelExpense

class TravelExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelExpense
        fields = ['id', 'trip', 'category', 'amount', 'date', 'note', 'created_at']