# urls.py
from django.urls import path
from hydrosonar.views import SensorDataView, ProcessedDataView, GraphicDataView

urlpatterns = [
    path('sensor-data/', SensorDataView.as_view(), name='sensor-data'),
    path('processed-data/', ProcessedDataView.as_view(), name='processed-data'),
    path('graphic-data/', GraphicDataView.as_view(), name='graphic-data'),
]
