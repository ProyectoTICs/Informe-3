from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re
from datetime import date
# Create your models here.
def validate_nombre(value):
    if len(value) < 3 :
        raise ValidationError('%s ->Nombre muy corto' % value)
    if  re.search(r"[0-9]", value) >= 0:
    	raise ValidationError('%s ->Se ingreso un caracter incorrecto' % value)
class Trabajador(models.Model):
	CafesComprados = models.IntegerField(null=True)
	Nombre = models.CharField(max_length=20,validators=[validate_nombre])
	Apellido = models.CharField(max_length=20,validators=[validate_nombre])
	Direccion = models.CharField(max_length=50)
	Cant_CafesConsumidos = models.IntegerField(null=True)
	Cant_CafesComprados = models.IntegerField(null=True)
    #FechaUltimaCompra = models.DateField(_("Date"), auto_now_add=True)


	def __unicode__(self):
		return (self.Nombre)
class Cafe(models.Model):
	Precio = models.IntegerField(null=True)
	Nombre = models.CharField(max_length=20)

	def __unicode__(self):
		return (self.Nombre)