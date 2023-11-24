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

# Função para gerar uma distância aleatória do sensor à água
def random_decimal():
    return random.uniform(0.1, altura_sem_tampa)  # Considerando a altura total da caixa como limite

# Gerar uma distância aleatória
distancia_sensor = random_decimal()

# Calcular o volume de água com base na distância do sensor
volume_agua = calcular_volume(distancia_sensor)

# Converter para litros
volume_litros = volume_agua * 1000  # Convertendo metros cúbicos para litros

# Calcular a porcentagem do volume em relação à capacidade máxima
porcentagem = (volume_litros / capacidade) * 100

print(f"Distância do sensor à água: {distancia_sensor:.2f} metros")
print(f"Volume de água na caixa: {volume_litros:.2f} litros")
print(f"Porcentagem do volume: {porcentagem:.2f}%")