from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Trabajador(models.Model):
	#GastoAcumulado = models.IntegerField(null=True)
	Nombre = models.CharField(max_length=20)
	Apellido = models.CharField(max_length=20)
	Direccion = models.CharField(max_length=50)

	def __unicode__(self):
		return (self.Nombre)
class Cafe(models.Model):
	Precio = models.IntegerField(null=True)
	Nombre = models.CharField(max_length=20)

	def __unicode__(self):
		return (self.Nombre)