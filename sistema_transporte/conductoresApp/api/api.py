from rest_framework.views import APIView
from rest_framework.decorators import api_view
from conductoresApp.api.serializers import ConductorSerializer
from conductoresApp.models import Conductor
from rest_framework import status
from rest_framework.response import Response
from vehiculosApp.api.serializers import VehiculoSerializer

from vehiculosApp.models import Vehiculo

@api_view(['GET', 'POST'])
def conductor_api_view(request):

    #List users
    if request.method == 'GET':        
        conductores = Conductor.objects.all().values('id', 'nombre','apellido', 'telefono', 'identicacion', 'direccion')
        conductores_serializer  = ConductorSerializer(conductores, many = True)
        return  Response(conductores_serializer.data, status= status.HTTP_200_OK)
    
    #Create user
    elif request.method == 'POST':
        print(request.method)
        conductores_serializer = ConductorSerializer(data = request.data)
        if conductores_serializer.is_valid():
            conductores_serializer.save()
            return Response(conductores_serializer.data,status= status.HTTP_201_CREATED)
        
        return Response(conductores_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def conductor_detail_view(request, pk):

    #Queryset (Consultar si el usuario existe)
    conductor = Conductor.objects.filter(id=pk).first()
    if conductor:

        #Find user by id
        if request.method == 'GET':
            conductor_serializer = ConductorSerializer(conductor)
            return Response(conductor_serializer.data, status=status.HTTP_200_OK)
        
        #Update user
        elif request.method == 'PUT':
            request.data
            conductor = Conductor.objects.filter(id=pk).first()
            conductor_serializer = ConductorSerializer(conductor, data = request.data)
            if conductor_serializer.is_valid():
                conductor_serializer.save()
                return Response(conductor_serializer.data , status= status.HTTP_200_OK)
            return Response(conductor_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        #Delete user
        elif request.method == 'DELETE':
            conductor = Conductor.objects.filter(id=pk).first()
            conductor.delete()
            return Response({'message': 'Conductor eliminado correctamente!'} , status= status.HTTP_200_OK)
    return Response({'message': 'No se ha encontrado un conductor con estos datos'}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def vehiculos_asignados(request, pk):

    #Queryset (Consultar si el usuario existe)
    vehiculos = Vehiculo.objects.filter(conductor_id = pk)
    if vehiculos:

        #Find user by id
        if request.method == 'GET':
            vehiculos_serializer =  VehiculoSerializer(vehiculos, many=True)
            return Response(vehiculos_serializer.data,status=status.HTTP_200_OK)
        
        #Update user
        elif request.method == 'PUT':
            request.data
            vehiculo = Vehiculo.objects.filter(id= request.data.get('id')).first()
            vehiculos_serializer = VehiculoSerializer(vehiculo, data = request.data)
            if vehiculos_serializer.is_valid():
                vehiculos_serializer.save()
                return Response(vehiculos_serializer.data , status= status.HTTP_200_OK)
            return Response(vehiculos_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    return Response({'message': 'No se ha encontrado un conductor con estos datos'}, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def vehiculos_no_asignados(request, pk):

    #Queryset (Consultar si el usuario existe)
    vehiculos = Vehiculo.objects.filter(conductor_id = None)
    if vehiculos:

        #Find user by id
        if request.method == 'GET':
            vehiculos_serializer =  VehiculoSerializer(vehiculos, many=True)
            return Response(vehiculos_serializer.data,status=status.HTTP_200_OK)
        
        #Update user
        elif request.method == 'PUT':
            request.data
            vehiculo = Vehiculo.objects.filter(id= request.data.get('id')).first()
            vehiculos_serializer = VehiculoSerializer(vehiculo, data = request.data)
            if vehiculos_serializer.is_valid() and vehiculo.conductor_id == None:
                vehiculos_serializer.save()
                return Response(vehiculos_serializer.data , status= status.HTTP_200_OK)
            return Response(vehiculos_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    return Response({'message': 'No se ha encontrado un conductor con estos datos'}, status = status.HTTP_400_BAD_REQUEST)