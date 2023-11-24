# sua_aplicacao/serializers.py
from rest_framework import serializers
from .models import DadoSensor, DadosGerais

class DadoSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadoSensor
        fields = ['valor_ultrassonico']

class DadosGeraisSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosGerais
        fields = ['nivel_agua_litros', 'consumo', 'identificacao_valvula']
