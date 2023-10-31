from rest_framework import serializers
from core.models import Usuario, Vehiculo, Viaje, Sede
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['nombreUsuario', 'rut', 'correo', 'nombre', 'apellidos', 'passUsuario','esConductor']

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['patente', 'modelo', 'marca','color','anno']


class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = ['nomSede', 'direccion']

class ViajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viaje
        fields = ['lugarInicio','nomSede','precio']