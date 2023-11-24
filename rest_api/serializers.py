from rest_framework import serializers
from core.models import Usuario, Vehiculo, Viaje

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['nombreUsuario', 'nombre', 'apellidos', 'passUsuario','esConductor']

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['patente','modelo','marca','color', 'anno']


class ViajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viaje
        fields = ['hora_salida','lugarInicio', 'destino', 'precio' ]