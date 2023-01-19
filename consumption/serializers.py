from rest_framework import serializers

from consumption.models import Consumption
from powermeter.serializers import PowerMeterSerializer


class ConsumptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consumption
        fields = ('timestamp', 'consumption')