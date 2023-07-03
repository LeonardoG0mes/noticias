from django.contrib import admin
from .models import Noticia

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_publicacao', 'nome_link', 'nome_link1', 'nome_link2', 'nome_link3', 'nome_link4')
    search_fields = ('titulo', 'autor', 'corpo')

admin.site.register(Noticia, NoticiaAdmin)
