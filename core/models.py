from django.db import models

# Create your models here.

class Usuario(models.Model):

    nombreUsuario = models.CharField(max_length=40, primary_key=True, unique=True, verbose_name="Nombre de Usuario")
    nombre = models.CharField(max_length=40, verbose_name="Nombre")
    apellidos = models.CharField(max_length=40, verbose_name="Apellidos") 
    passUsuario = models.CharField(max_length=20, verbose_name="Contraseña")
    esConductor = models.BooleanField(default=False, verbose_name="Es Conductor")

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    
class Vehiculo(models.Model):
    patente = models.CharField(max_length=8, verbose_name="Patente", primary_key=True, unique=True,) 
    modelo = models.CharField(max_length=15, verbose_name="Modelo Vehiculo")
    marca = models.CharField(max_length=15,  verbose_name="Marca Vehiculo")
    color = models.CharField(max_length=15,  verbose_name="Color_Vehiculo")
    anno = models.IntegerField( verbose_name="Año Vehiculo")
    def __str__(self):
        return f"{self.marca} Patente:{self.patente}"
    
class Viaje(models.Model):
    hora_salida = models.TimeField( verbose_name="Hora de salida")
    lugarInicio = models.CharField(max_length=30,  verbose_name="Lugar inicio")
    destino = models.CharField(max_length=30,  verbose_name="Destino Viaje")
    precio = models.PositiveIntegerField( verbose_name="Precio")

    def __str__(self):
        return f"Viaje de Usuario a {self.destino} a las {self.hora_salida}"
    
    
