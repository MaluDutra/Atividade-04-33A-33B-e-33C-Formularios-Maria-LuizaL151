from django.contrib import admin
from .models import FilmesFamosos, TopFilmes, Nomeados


# Register your models here.
admin.site.register(FilmesFamosos)
admin.site.register(TopFilmes)
admin.site.register(Nomeados)
