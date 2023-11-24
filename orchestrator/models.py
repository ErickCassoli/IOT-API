from django.db import models

class DadoSensor(models.Model):
    valor_ultrassonico = models.FloatField()

class DadosGerais(models.Model):
    nivel_agua_litros = models.FloatField()
    consumo = models.IntegerField()
    identificacao_valvula = models.CharField(max_length=20)
class ConsumoHora(models.Model):
    hora = models.DateTimeField(auto_now_add=True)
    consumo = models.IntegerField()