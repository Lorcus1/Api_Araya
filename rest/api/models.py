from django.db import models
from django.db.models.fields import DateField

class Libro(models.Model):
    ID       = models.AutoField(primary_key=True)
    Nombre   = models.CharField(max_length=99)
    Autor    = models.CharField(max_length=99)
    Sinopsis = models.TextField()
    Precio   = models.IntegerField(default=0)
    Stock    = models.IntegerField(default=0)
    Publicación = models.DateField()
