from django.db import models

# Create your models here.

class Usuario(models.Model):

    nombreUsuario = models.CharField(max_length=40, primary_key=True, unique=True,)
    rut = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    passUsuario = models.CharField(max_length=20)
    esConductor = models.BooleanField()

    def __str__(self):
        return self.nombreUsuario
    
class Vehiculo(models.Model):
    patente = models.CharField(max_length=8, primary_key=True, unique=True,) 
    modelo = models.CharField(max_length=15)
    marca = models.CharField(max_length=15)
    color = models.CharField(max_length=15)
    anno = models.IntegerField()
    def __str__(self):
        return self.patente

class Sede(models.Model):
    nomSede = models.CharField(max_length=30, primary_key=True, unique=True,)
    direccion = models.CharField(max_length=40)

    def __str__(self):
        return self.nomSede
    
class Viaje(models.Model):
    lugarInicio = models.CharField(max_length=30)
    nomSede = models.ForeignKey(Sede, on_delete=models.CASCADE, max_length=30)
    precio = models.PositiveIntegerField()

    def __str__(self):
        return self.lugarInicio
