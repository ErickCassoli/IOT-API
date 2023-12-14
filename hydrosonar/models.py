from django.db import models
from django.utils import timezone
import pytz

class SensorData(models.Model):
    value = models.FloatField()
    timestamp = models.DateTimeField()

    def save(self, *args, **kwargs):
        # Define o fuso horário desejado (por exemplo, 'America/Sao_Paulo')
        tz = pytz.timezone('America/Sao_Paulo')

        # Obtém a data e hora atuais no fuso horário desejado
        timestamp_with_timezone = timezone.now().astimezone(tz)

        # Atribui o timestamp ao objeto SensorData
        self.timestamp = timestamp_with_timezone
        super().save(*args, **kwargs)

class ProcessedData(models.Model):
    sensor_data = models.OneToOneField(SensorData, on_delete=models.CASCADE, primary_key=True)
    volume_liters = models.FloatField()
    percent_water = models.FloatField()  # Corrigi o nome do campo
    valve_state = models.BooleanField()
