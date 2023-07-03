from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:noticia_id>/', views.noticia, name='noticia'),
    path('noticias/', views.noticias, name='noticias'),
    path('contato/', views.contato, name='contato'),

]
