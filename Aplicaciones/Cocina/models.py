import uuid
from django.db import models

# Create your models here.

class Receta(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_receta = models.CharField(max_length=50)
    calificacion = models.PositiveSmallIntegerField()
    imagen = models.ImageField(upload_to="recetas", null=True)
 
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre_receta, self.calificacion)