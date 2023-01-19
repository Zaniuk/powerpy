from rest_framework import serializers

from powermeter.models import PowerMeter


class PowerMeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerMeter
        fields = ('meter_id', 'name')
