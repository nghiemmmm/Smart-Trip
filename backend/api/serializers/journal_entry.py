from rest_framework import serializers
from api.models.journal_entry import JournalEntry

class JournalEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEntry
        fields = ['id', 'trip', 'date', 'content', 'created_at']