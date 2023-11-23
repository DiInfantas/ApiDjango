from rest_framework import serializers
from core.models import Usuario, Vehiculo, Viaje, Sede
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['nombreUsuario','correo' , 'nombre', 'apellidos', 'passUsuario','esConductor']

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class ViajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viaje
        fields = '__all__'