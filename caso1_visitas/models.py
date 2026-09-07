from django.db import models

# Create your models here.
class Visita(models.Model):
    nombre= models.CharField(max_length=15)
    rut= models.IntegerField(default=0, primary_key=True)
    motivo_visita= models.CharField(max_length=320)
    hora_entrada_salida= models.TimeField(verbose_name="Selecciona la hora")