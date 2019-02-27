from django.db import models

# Create your models here.

class Jugador(models.Model):
	content = models.CharField(max_length=256)
	apellido = models.CharField(max_length=256)
	edad = models.CharField(max_length=256)
	estatura = models.CharField(max_length=256)
	nacionalidad = models.CharField(max_length=256)
	equipo = models.CharField(max_length=256)
	universidad = models.CharField(max_length=256)
	posicion = models.CharField(max_length=256)

	timestamp = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.content
		

class Equipo(models.Model):
	content = models.CharField(max_length=256)
	liga = models.CharField(max_length=256)
	estado = models.CharField(max_length=256)
	campionatos = models.CharField(max_length=256)

	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.content
		

class Estadio(models.Model):
	content = models.CharField(max_length=256)
	ubicacion = models.CharField(max_length=256)
	capacidad = models.CharField(max_length=256)
	equipo_local = models.CharField(max_length=256)

	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.content


