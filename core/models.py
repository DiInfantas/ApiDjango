from django.db import models

# Create your models here.

class Usuario(models.Model):

    nombreUsuario = models.CharField(max_length=40, primary_key=True, unique=True)
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40) 
    passUsuario = models.CharField(max_length=20)
    esConductor = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    
class Vehiculo(models.Model):
    patente = models.CharField(max_length=8, primary_key=True, unique=True,) 
    modelo = models.CharField(max_length=15)
    marca = models.CharField(max_length=15)
    color = models.CharField(max_length=15)
    anno = models.IntegerField()
    def __str__(self):
        return f"{self.marca} Patente:{self.patente}"
    
class Viaje(models.Model):
    hora_salida = models.TimeField()
    lugarInicio = models.CharField(max_length=30)
    destino = models.CharField(max_length=30)
    precio = models.PositiveIntegerField()

    def __str__(self):
        return f"Viaje de Usuario a {self.destino} a las {self.hora_salida}"
