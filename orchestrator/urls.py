from django.urls import path
from .views import atualizar_sensor, obter_dados

urlpatterns = [
    path('atualizar_sensor/', atualizar_sensor, name='atualizar_sensor'),
    path('obter_dados/', obter_dados, name='obter_dados'),
]
