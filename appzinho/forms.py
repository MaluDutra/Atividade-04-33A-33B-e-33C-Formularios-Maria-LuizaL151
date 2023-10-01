from django.forms import ModelForm
from .models import FilmesFamosos

class FilmesForm(ModelForm):
  class Meta:
    model = FilmesFamosos
    fields =["title","main_character","genre","release_date"]