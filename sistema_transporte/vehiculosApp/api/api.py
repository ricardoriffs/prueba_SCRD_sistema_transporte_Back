from rest_framework.views import APIView
from rest_framework.decorators import api_view
from vehiculosApp.api.serializers import VehiculoSerializer
from vehiculosApp.models import Vehiculo
from rest_framework import status
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def vehiculo_api_view(request):

    #List users
    if request.method == 'GET':        
        vehiculos = Vehiculo.objects.all()
        vehiculos_serializer  = VehiculoSerializer(vehiculos, many = True)
        return  Response(vehiculos_serializer.data, status= status.HTTP_200_OK)
    
    #Create user
    elif request.method == 'POST':
        vehiculos_serializer = VehiculoSerializer(data = request.data)
        if vehiculos_serializer.is_valid():
            vehiculos_serializer.save()
            return Response(vehiculos_serializer.data,status= status.HTTP_201_CREATED)
        
        return Response(vehiculos_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def vehiculo_detail_view(request, pk):

    #Queryset (Consultar si el usuario existe)
    vehiculo = Vehiculo.objects.filter(id=pk).first()
    if vehiculo:

        #Find user by id
        if request.method == 'GET':
            vehiculos_serializer = VehiculoSerializer(vehiculo)
            return Response(vehiculos_serializer.data, status=status.HTTP_200_OK)
        
        #Update user
        elif request.method == 'PUT':
            request.data
            vehiculo = Vehiculo.objects.filter(id=pk).first()
            vehiculos_serializer = VehiculoSerializer(vehiculo, data = request.data)
            if vehiculos_serializer.is_valid():
                vehiculos_serializer.save()
                return Response(vehiculos_serializer.data , status= status.HTTP_200_OK)
            return Response(vehiculos_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        #Delete user
        elif request.method == 'DELETE':
            vehiculo = Vehiculo.objects.filter(id=pk).first()
            vehiculo.delete()
            return Response({'message': 'Conductor eliminado correctamente!'} , status= status.HTTP_200_OK)
    return Response({'message': 'No se ha encontrado un conductor con estos datos'}, status = status.HTTP_400_BAD_REQUEST)