from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Disquera(models.Model):
    nombre= models.CharField(max_length=30)
    domicilio= models.CharField(max_length=50)
    ciudad= models.CharField(max_length=60)
    estado= models.CharField(max_length=30)
    pais= models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

class Autor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()

    def NombreCompleto(self):
        cadena = "{0} {1}, {2}"

        #cadena= "%s %s" %(self.nombre, self.apellido)
        return cadena.format(self.nombre, self.apellido)
    def __str__(self):
        return self.NombreCompleto()

class Cancion(models.Model):
    titulo= models.CharField(max_length=30)
    autores= models.ManyToManyField(Autor)
    disquera= models.ForeignKey('Disquera', on_delete=models.PROTECT)
    fecha_publicacion= models.DateField()
    portada= models.ImageField(blank=True)
    #portada= models.ImageField(upload_to= 'portadas/')

    def __unicode__(self):
        return self.titulo


    
        
