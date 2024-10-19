from django.db import models

# Create your models here.


class Genero(models.Model):
    genero_id = models.AutoField(primary_key=True)
    genero_usuario = models.CharField(max_length=255)
    class Mete:
        db_tabla = 'genero'
        
class Usuarios(models.Model):
    usarios_id = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=255)
    fk_genero = models.ForeignKey(Genero,on_delete=models.CASCADE,default=0)
    class Mete:
        db_tabla = 'usuarios'