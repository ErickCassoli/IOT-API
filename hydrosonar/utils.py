from datetime import datetime, timedelta
from .models import SensorData, ProcessedData

# Medidas do recipiente
comprimento_recipiente = 25.8  # cm
largura_recipiente = 17.8  # cm
altura_recipiente = 8.5  # cm

# Estado inicial da válvula (pode ser ajustado conforme necessário)
valvula_ativa_inicial = False

# Função para calcular o volume do recipiente em litros
def calcular_volume_litros(distancia_sensor_agua):
    # Calcular a altura atual da água no recipiente
    altura_agua_atual = altura_recipiente - distancia_sensor_agua

    # Calcular o volume em litros
    volume_cm3 = comprimento_recipiente * largura_recipiente * altura_agua_atual
    volume_litros = volume_cm3 / 1000
    
    return volume_litros

# Função para calcular a porcentagem do nível de água
def calcular_porcentagem_nivel(distancia_sensor_agua):
    # Calcular a altura atual da água no recipiente
    altura_agua_atual = altura_recipiente - distancia_sensor_agua

    # Calcular a porcentagem do nível de água
    porcentagem_nivel = (altura_agua_atual / altura_recipiente) * 100
    
    return porcentagem_nivel

# Função para processar os dados do sensor e atualizar o banco de dados
def process_sensor_data():
    # Último dado do sensor
    ultimo_dado = SensorData.objects.latest('timestamp')
    
    # Distância do sensor até a água
    distancia_sensor_agua = ultimo_dado.value
    
    # Calcular o volume em litros
    volume_litros = calcular_volume_litros(distancia_sensor_agua)
    
    # Calcular a porcentagem do nível de água
    porcentagem_nivel = calcular_porcentagem_nivel(distancia_sensor_agua)
    
    # Obter o último dado processado para verificar o estado anterior da válvula
    try:
        ultimo_dado_processado = ProcessedData.objects.latest('sensor_data__timestamp')
        valvula_anterior_ativa = ultimo_dado_processado.valve_state
    except ProcessedData.DoesNotExist:
        valvula_anterior_ativa = valvula_ativa_inicial

    # Verificar se a válvula deve estar ativa
    if porcentagem_nivel < 10 and not valvula_anterior_ativa:
        valvula_ativa = True
    elif porcentagem_nivel >= 90 and valvula_anterior_ativa:
        valvula_ativa = False
    else:
        valvula_ativa = valvula_anterior_ativa

    # Criar um novo objeto ProcessedData associado ao último SensorData
    ProcessedData.objects.create(
        sensor_data=ultimo_dado,
        volume_liters=volume_litros,
        percent_watter=porcentagem_nivel,
        valve_state=valvula_ativa
    )

# Função para obter os dados processados
def get_all_processed_data():
    # Obter todos os dados processados ordenados por timestamp do SensorData
    all_processed_data = ProcessedData.objects.order_by('sensor_data__timestamp')

    # Serializar os dados para retornar no formato desejado (JSON)
    processed_data_list = []
    for processed_data in all_processed_data:
        data_entry = {
            'timestamp': processed_data.sensor_data.timestamp,
            'percent': processed_data.percent_watter,
            'liters': processed_data.volume_liters,
            'valve_state': processed_data.valve_state
        }
        processed_data_list.append(data_entry)

    return processed_data_list