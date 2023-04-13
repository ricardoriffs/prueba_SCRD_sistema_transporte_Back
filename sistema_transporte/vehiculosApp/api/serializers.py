from vehiculosApp.models import Vehiculo
from rest_framework import serializers

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Vehiculo
        fields = ('id', 'modelo', 'placa', 'capacidad', 'conductor_id')