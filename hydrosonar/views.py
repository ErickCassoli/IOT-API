from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import SensorData
from .serializer import SensorDataSerializer
from .utils import process_sensor_data, get_processed_data, get_graphic_data


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

        # Retornar os dados para o front-end em formato JSON
        return Response(processed_data)

class GraphicDataView(APIView):
    def get(self, request, format=None):
        # Obter os dados processados para o sensor
        graphicData = get_graphic_data()

        # Retornar os dados para o front-end em formato JSON
        return Response(graphicData)