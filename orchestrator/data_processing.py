import math

# Dados do retângulo
comprimento = 25.8  # cm
largura = 17.8  # cm
altura = 8.5  # cm
capacidade_maxima_litros = 2.5  # Capacidade máxima em litros
capacidade_maxima_cm3 = capacidade_maxima_litros * 1000  # Capacidade máxima em cm³
altura_sensor_tampa = 3  # Altura do sensor acima da tampa

# Função para calcular o volume com base na altura da água no retângulo
def calcular_volume(distancia_sensor_agua):
    altura_agua = altura - (distancia_sensor_agua - altura_sensor_tampa)  # Considerando a altura da água como a diferença entre a altura total e a medida do sensor ajustada pela altura do sensor acima da tampa

    altura_agua = max(altura_agua, 0)  # Garantir que a altura não seja negativa
    altura_agua = min(altura_agua, altura)  # Garantir que a altura da água não ultrapasse a altura total do retângulo

    volume = comprimento * largura * altura_agua
    return volume



leituras_sensor = [
    0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.5, 0.75, 0.9, 1.0, 1.1, 1.2, 1.15, 1.1, 1.05, 1.0
]
def verificar_enchimento(leituras_sensor):
    aumento_detectado = False

    for i in range(1, len(leituras_sensor)):
        if leituras_sensor[i] > leituras_sensor[i - 1]:
            aumento_detectado = True
            break  

    return aumento_detectado



def processar_dados_sensor(valor):
    altura_sensor_agua = valor + altura_sensor_tampa  # Altura do sensor até a superfície da água

    volume_agua = calcular_volume(altura_sensor_agua)

    porcentagem = (volume_agua / capacidade_maxima_cm3) * 100

    identificacao_valvula = valor < altura  # Verifica se a altura da água é menor que a altura total do retângulo

    consumo = capacidade_maxima_cm3 - volume_agua

    dados_json = {
        "nivel_agua_cm3": volume_agua,
        "consumo": consumo,
        "identificacao_valvula": identificacao_valvula,
        "Porcentagem": porcentagem
    }

    return dados_json