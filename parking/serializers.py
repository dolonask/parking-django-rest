

from rest_framework import serializers
from .models import Tariff, Operation

from .models import statuses


class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = '__all__'


class OperationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    add_date = serializers.DateTimeField(required=False)
    edit_date = serializers.DateTimeField(required=False)
    car_number = serializers.CharField(max_length=20)
    status = serializers.ChoiceField(choices=statuses, default='OPEN')

    def create(self, validated_data):
        return Operation.objects.create(**validated_data)
