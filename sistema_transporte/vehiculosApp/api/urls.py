from django.urls import path
from vehiculosApp.api.api import vehiculo_api_view, vehiculo_detail_view

urlpatterns = [
    path('vehiculo/', vehiculo_api_view, name='vehiculos_api'),
    path("vehiculo/<int:pk>/", vehiculo_detail_view, name="vehiculo_detail_view")
]