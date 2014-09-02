from django.db import models

# Create your models here.
class Trabajador(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    rut = models.CharField(max_length=50, primary_key= True)
    gasto_acumulado = models.IntegerField()
    def __unicode__(self):
    return (self.nombre)