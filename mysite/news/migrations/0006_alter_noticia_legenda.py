# Generated by Django 4.2.3 on 2023-07-04 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_noticia_legenda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='legenda',
            field=models.CharField(choices=[('esporte', 'Esporte'), ('entretenimento', 'Entretenimento'), ('política', 'Política'), ('economia', 'Economia'), ('tecnologia', 'Tecnologia'), ('saúde', 'Saúde'), ('ciência', 'Ciência'), ('educação', 'Educação'), ('meio_ambiente', 'Meio Ambiente'), ('cultura', 'Cultura')], max_length=50),
        ),
    ]
