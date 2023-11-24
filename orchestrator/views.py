# sua_aplicacao/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import DadoSensor, DadosGerais, ConsumoHora
from .serializers import DadoSensorSerializer, DadosGeraisSerializer
from .dataprocessing import processar_dados_sensor
from datetime import datetime, timedelta

@csrf_exempt
def atualizar_sensor(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DadoSensorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            # Chama a função de processamento de dados
            nivel_agua_litros, consumo, identificacao_valvula = processar_dados_sensor(data["valor_ultrassonico"])

            # Atualiza os dados gerais ou cria um novo objeto
            dados_gerais, created = DadosGerais.objects.get_or_create(id=1)
            dados_gerais.nivel_agua_litros = nivel_agua_litros
            dados_gerais.consumo = consumo
            dados_gerais.identificacao_valvula = identificacao_valvula
            dados_gerais.save()

            # Adiciona o consumo por hora
            hora_atual = datetime.now().replace(minute=0, second=0, microsecond=0)
            consumo_hora, created = ConsumoHora.objects.get_or_create(hora=hora_atual)
            consumo_hora.consumo += consumo
            consumo_hora.save()

            return JsonResponse({"success": True})
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def obter_dados(request):
    dados_gerais = DadosGerais.objects.first()  # Obtém o primeiro objeto, você pode ajustar conforme necessário
    serializer_gerais = DadosGeraisSerializer(dados_gerais)

    # Obtém dados de consumo por hora nas últimas 24 horas
    hora_atual = datetime.now().replace(minute=0, second=0, microsecond=0)
    hora_inicial = hora_atual - timedelta(hours=23)

    consumo_horas = ConsumoHora.objects.filter(hora__range=(hora_inicial, hora_atual))
    consumo_horas_data = [{"hora": hora.consumo, "consumo": hora.consumo} for hora in consumo_horas]

    return JsonResponse({
        "dados_gerais": serializer_gerais.data,
        "consumo_horas": consumo_horas_data
    })
