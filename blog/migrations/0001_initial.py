# Generated by Django 3.0.6 on 2020-05-29 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('conteudo', models.TextField(verbose_name='Conteúdo')),
                ('imagem', models.ImageField(upload_to='imagens/')),
                ('data_criacao', models.DateTimeField(auto_now=True, verbose_name='Data de criação')),
                ('data_atualizacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de atualizacao')),
            ],
        ),
    ]
