# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import SensorData
from .serializer import SensorDataSerializer
from .utils import process_sensor_data, get_processed_data, calcular_consumo_24h

class SensorDataView(APIView):
    def post(self, request, format=None):
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            process_sensor_data()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProcessedDataView(APIView):
    def get(self, request, format=None):
        # Obter os dados processados
        processed_data = get_processed_data()

        # Calcular o consumo em 24 horas
        consumo_24h = calcular_consumo_24h()
        
        # Adicionar os dados de consumo em 24 horas aos dados processados
        processed_data['consumo_24h'] = consumo_24h

        # Retornar os dados para o front-end em formato JSON
        return Response(processed_data)
