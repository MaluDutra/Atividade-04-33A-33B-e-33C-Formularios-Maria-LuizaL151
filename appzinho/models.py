from django.db import models

# Create your models here.
class FilmesFamosos(models.Model):
  title = models.CharField(max_length=50)
  main_character = models.CharField(max_length=50)
  genre = models.CharField(max_length=20)
  release_date = models.DateField()


class TopFilmes(models.Model):
  OPTIONS = [
    ("S", "Sad"),
    ("H", "Happy"),
    ("M", "Mixed"),
  ]
  title = models.CharField(max_length=50)
  main_character = models.CharField(max_length=50)
  feelings = models.CharField(max_length=1, choices=OPTIONS)
  position_in_top = models.IntegerField()
  release_date = models.DateField()

class Nomeados(models.Model):
  title = models.CharField(max_length=50)
  nominated = models.CharField(max_length=10)
  year = models.PositiveIntegerField()
