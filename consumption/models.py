from django.db import models

from powermeter.models import PowerMeter


class Consumption(models.Model):
    id = models.AutoField(primary_key=True)
    consumption = models.FloatField()
    timestamp = models.DateTimeField()
    meter = models.ForeignKey(PowerMeter, to_field='meter_id', on_delete=models.CASCADE)
