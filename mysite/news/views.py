from django.shortcuts import render, get_object_or_404
from .models import Noticia

def home(request):
    noticias = Noticia.objects.filter(home=True).order_by('-data_publicacao')[:7]
    context = {
        'noticias': noticias
    }
    return render(request, 'home.html', context)

def detalhes(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    context = {
        'noticia': noticia
    }
    return render(request, 'detalhes_noticias.html', context)

def esportes(request):
    noticias_esportes = Noticia.objects.filter(legenda='esporte').order_by('-data_publicacao')
    context = {
        'noticias': noticias_esportes
    }
    return render(request, 'esportes.html', context)

def entretenimento(request):
    sub_legendas = ['Musica', 'Cinema', 'Fofoca', 'Séries', 'Desenhos']  # Lista de sub-legendas

    noticias = Noticia.objects.filter(legenda='entretenimento').order_by('-data_publicacao')

    context = {
        'sub_legendas': sub_legendas,
        'noticias': noticias
    }

    return render(request, 'entretenimento.html', context)

def politica(request):
    noticias_politica = Noticia.objects.filter(legenda='política').order_by('-data_publicacao')
    context = {
        'noticias': noticias_politica
    }
    return render(request, 'politica.html', context)

def contato(request):
    return render(request, 'contato.html')
