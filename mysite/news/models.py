from django.db import models

class Noticia(models.Model):
    LEGENDA_CHOICES = (
        ('esporte', 'Esporte'),
        ('entretenimento', 'Entretenimento'),
        ('política', 'Política'),
        ('economia', 'Economia'),
        ('tecnologia', 'Tecnologia'),
        ('saúde', 'Saúde'),
        ('ciência', 'Ciência'),
        ('educação', 'Educação'),
        ('meio_ambiente', 'Meio Ambiente'),
        ('cultura', 'Cultura'),
        ('aleatorio', 'Acontecimento Aleatório'),
        # Adicione outros tipos de legenda conforme necessário
    )
    legenda = models.CharField(max_length=50, choices=LEGENDA_CHOICES)
    titulo = models.CharField(max_length=200)
    resumo = models.CharField(max_length=500, blank=True)
    corpo = models.TextField()
    imagem = models.ImageField(upload_to='noticias')
    autor = models.CharField(max_length=100)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=200, blank=True)
    nome_link = models.CharField(max_length=200, blank=True)
    link1 = models.CharField(max_length=200, blank=True)
    nome_link1 = models.CharField(max_length=200, blank=True)
    link2 = models.CharField(max_length=200, blank=True)
    nome_link2 = models.CharField(max_length=200, blank=True)
    link3 = models.CharField(max_length=200, blank=True)
    nome_link3 = models.CharField(max_length=200, blank=True)
    link4 = models.CharField(max_length=200, blank=True)
    nome_link4 = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.titulo
