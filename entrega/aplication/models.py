from django.db import models

# Create your models here.

class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    abreviatura = models.CharField(max_length=6)
    ciudad = models.CharField(max_length=60)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.nombre},{self.ciudad}"

class Jugador(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    equipo = models.CharField(max_length=60)
    edad = models.CharField(max_length=2)
    
    class Meta:
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"
        ordering = ["id"]


    def __str__(self):
        return f"{self.apellido}, {self.nombre}, {self.edad}"

class DirectorTecnico(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()
    equipo = models.CharField(max_length=60)

    class Meta:
        verbose_name = "DirectorTecnico"
        verbose_name_plural = "DirectoresTecnicos"
        ordering = ["id"]

    def __str__(self):
        return f"{self.apellido}, {self.nombre}" 
