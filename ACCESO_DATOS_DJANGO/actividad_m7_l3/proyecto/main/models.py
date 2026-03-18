from django.db import models

# Create your models here.

class Autor(models.Model):
 
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    biografia = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.nombre}'

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)