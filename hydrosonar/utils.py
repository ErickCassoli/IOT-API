from datetime import datetime, timedelta
from .models import SensorData, ProcessedData

# Medidas do recipiente
comprimento_recipiente = 25.8  # cm
largura_recipiente = 17.8  # cm
altura_recipiente = 8.5  # cm

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
    
    # Verificar se a válvula deve estar ativa
    valvula_ativa = porcentagem_nivel <= 10
    
    # Criar um novo objeto ProcessedData associado ao último SensorData
    ProcessedData.objects.create(
        sensor_data=ultimo_dado,
        volume_litros=volume_litros,
        porcentagem_agua=porcentagem_nivel,  # Agora armazenamos a porcentagem do nível
        valvula_ativa=valvula_ativa
    )

# ... (restante do código)

def calcular_consumo_24h():
   # Obtendo os dados dos últimos 24 horas
    agora = datetime.now()
    data_inicio = agora - timedelta(days=1)
    
    # Filtrando os dados do banco de dados para o período desejado
    dados_24h = SensorData.objects.filter(timestamp__gte=data_inicio, timestamp__lte=agora).order_by('timestamp')
    
    # Calculando o consumo em cada hora
    consumo_por_hora = []
    hora_atual = data_inicio

    for dado in dados_24h:
        # Calculando a diferença em litros entre as leituras consecutivas
        if consumo_por_hora:
            litros_consumidos = dado.volume_litros - consumo_por_hora[-1][1]
        else:
            litros_consumidos = 0
        
        # Adicionando a hora e o consumo à lista
        consumo_por_hora.append((hora_atual.strftime('%H:%M'), litros_consumidos))
        
        # Atualizando a hora atual para a próxima iteração
        hora_atual += timedelta(hours=1)

    return consumo_por_hora

# Função para obter os dados processados
def get_processed_data():
    # Obter os dados processados
    ultimo_dado_processado = ProcessedData.objects.latest('sensor_data__timestamp')

    # Retornar um dicionário com os dados processados
    return {
        'consumo_24h': calcular_consumo_24h(),
        'nivel_atual': {
            'porcentagem': ultimo_dado_processado.porcentagem_agua,
            'litros': ultimo_dado_processado.volume_litros
        },
        'valvula_ativa': ultimo_dado_processado.valvula_ativa
    }
