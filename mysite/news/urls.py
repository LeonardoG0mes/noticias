from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:noticia_id>/', views.detalhes, name='noticia'),
    path('esportes/', views.esportes, name='esportes'),
    path('contato/', views.contato, name='contato'),
    path('entretenimento/', views.entretenimento, name='entretenimento'),
    path('politica/', views.politica, name='politica'),

]
