from django.db import models


# Create your models here.

# Consumptions are a list of Consumption objects

class PowerMeter(models.Model):
    id = models.AutoField(primary_key=True)
    meter_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
