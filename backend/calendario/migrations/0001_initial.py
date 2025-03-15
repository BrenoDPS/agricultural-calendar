# Generated by Django 5.1.2 on 2024-10-15 23:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bandeja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cultura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plantio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especie', models.CharField(max_length=100)),
                ('celula', models.CharField(max_length=10)),
                ('produtividade', models.FloatField()),
                ('variedade', models.CharField(max_length=100)),
                ('data_plantio', models.DateField()),
                ('data_colheita', models.DateField(blank=True, null=True)),
                ('bandeja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendario.bandeja')),
                ('cultura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendario.cultura')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notificacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem', models.CharField(max_length=255)),
                ('enviada', models.BooleanField(default=False)),
                ('data_notificacao', models.DateTimeField()),
                ('plantio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendario.plantio')),
            ],
        ),
    ]
