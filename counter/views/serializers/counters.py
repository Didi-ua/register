from rest_framework import serializers

from counter.models import Counter, History


class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = '__all__'
        read_only_fields = ('id', 'user')

    def update(self, instance, validated_data):
        if validated_data.get('current_value'):
            if validated_data['current_value'] < instance.current_value:
                validated_data['current_value'] = instance.current_value
                raise serializers.ValidationError('value cannot decrease')
            elif validated_data['current_value'] != instance.current_value:
                History.objects.create(
                    type=History.UserType.USER,
                    value=validated_data['current_value'],
                    consumption=validated_data['current_value'] - instance.current_value,
                    counter=instance
                )
        return super().update(instance, validated_data)
