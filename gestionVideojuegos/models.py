from django.db import models

# Create your models here.

class videojuegos(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(default="Sin descripción") 
    fecha_lanzamiento = models.DateField(null=True, blank=True)
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    precio = models.IntegerField()
    video = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.titulo