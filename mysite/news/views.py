from django.shortcuts import render, get_object_or_404
from .models import Noticia

def home(request):
    noticias = Noticia.objects.order_by('-data_publicacao')[:7]
    context = {
        'noticias': noticias
    }
    return render(request, 'home.html', context)

def noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    context = {
        'noticia': noticia
    }
    return render(request, 'detalhes_noticias.html', context)

def noticias(request):
    noticias = Noticia.objects.order_by('-data_publicacao')
    context = {
        'noticias': noticias
    }
    return render(request, 'noticias.html', context)


def contato(request):
    return render(request, 'contato.html')
    
