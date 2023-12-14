from django.db import models
from django.utils import timezone
import pytz

class SensorData(models.Model):
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
class ProcessedData(models.Model):
    sensor_data = models.OneToOneField(SensorData, on_delete=models.CASCADE, primary_key=True)
    volume_liters = models.FloatField()
    percent_water = models.FloatField()  # Corrigi o nome do campo
    valve_state = models.BooleanField()
