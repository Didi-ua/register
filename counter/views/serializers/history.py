from rest_framework import serializers
from counter.models import History


class HistorySerializer(serializers.ModelSerializer):
    period = serializers.DateTimeField(format='%d.%m.%Y')

    class Meta:
        model = History
        fields = ['period', 'consumption', 'value', 'type']
