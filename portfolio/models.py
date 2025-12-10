from django.db import models

from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    imagen = models.ImageField(verbose_name="Imagen", upload_to="proyectos")
    url = models.URLField(verbose_name="Enlace", null=True, blank=True)

    
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    def __str__(self):
        return self.titulo
class Proyecto(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    imagen = models.ImageField(verbose_name="Imagen", upload_to="proyectos")
    url = models.URLField(verbose_name="Enlace", null=True, blank=True)

   
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    def __str__(self):
        return self.titulo
