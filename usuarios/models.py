from django.db import models

# Create your models here.


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos/')
