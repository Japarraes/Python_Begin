from django.db import models
from django.urls import reverse

# Create your models here.

# Create your models here.
class Genre(models.Model):
    
    name = models.CharField(max_length=64, help_text="Pon el nombre del género")

    def __str__(self):
        
        return self.name
        
class Movie(models.Model):

    title = models.CharField(max_length=64)
    director = models.ForeignKey('director', on_delete=models.SET_NULL, null=True)
    sinopsis = models.TextField(max_length=100, help_text="Indiqua el argumento del libro")
    genre = models.ManyToManyField(Genre)
    year = models.IntegerField(max_length=4, help_text="Año de estreno")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie-detail", args=[str(self.id)])


# Clase Director
class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse("director-detail", args=[str(self.id)])
        
    def __str__(self):
        return "%s (%s)" % (self.last_name, self.first_name)