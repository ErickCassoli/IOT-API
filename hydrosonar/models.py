from django.db import models

class SensorData(models.Model):
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
class ProcessedData(models.Model):
    sensor_data = models.OneToOneField(SensorData, on_delete=models.CASCADE, primary_key=True)
    volume_liters = models.FloatField()
    percent_watter = models.FloatField()
    valve_state = models.BooleanField()
