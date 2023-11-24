import math
import random

# Dados da caixa d'água
altura_sem_tampa = 0.58  # Altura sem tampa
diametro_com_tampa = 1.24  # Diâmetro com a tampa
diametro_sem_tampa = 1.22  # Diâmetro sem a tampa
diametro_base = 0.95  # Diâmetro da base
capacidade = 500  # Capacidade em litros

# Função para calcular o volume com base na altura da água
def calcular_volume(distancia_sensor_agua):
    raio_com_tampa = diametro_com_tampa / 2
    raio_sem_tampa = diametro_sem_tampa / 2

    altura_agua = altura_sem_tampa - (altura_sem_tampa * (distancia_sensor_agua / altura_sem_tampa))
    altura_agua = max(altura_agua, 0)  # Garantir que a altura não seja negativa

    raio_agua = raio_sem_tampa * (altura_agua / altura_sem_tampa)

    volume = (math.pi / 3) * altura_agua * (raio_agua ** 2 + raio_agua * raio_com_tampa + raio_com_tampa ** 2)
    return volume


leituras_sensor = [
    0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.5, 0.75, 0.9, 1.0, 1.1, 1.2, 1.15, 1.1, 1.05, 1.0
]
def verificar_enchimento(leituras_sensor):
    aumento_detectado = False

    for i in range(1, len(leituras_sensor)):
        if leituras_sensor[i] > leituras_sensor[i - 1]:
            aumento_detectado = True
            break  # Se detectar aumento, interrompe o loop

    return aumento_detectado

def processar_dados_sensor(valor):
    volume_agua = calcular_volume(valor)

    nivel_agua_litros = volume_agua * 1000  

    porcentagem = (nivel_agua_litros / capacidade) * 100

    identificacao_valvula = verificar_enchimento(valor)

    consumo = capacidade - nivel_agua_litros

    dados_json = {
        "nivel_agua_litros": nivel_agua_litros,
        "consumo": consumo,
        "identificacao_valvula": identificacao_valvula
    }

    return dados_json