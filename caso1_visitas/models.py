from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime, timedelta

# Create your models here.
class Visita(models.Model):
    nombre = models.CharField(max_length=15)
    rut = models.IntegerField(
        primary_key=True,
        validators=[
            MinValueValidator(70000000),
            MaxValueValidator(259999999),
        ],
    )
    motivo_visita = models.CharField(max_length=320)
    hora_entrada = models.DateTimeField()
    
