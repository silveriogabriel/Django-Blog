# Generated by Django 4.0.1 on 2022-01-31 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='simulacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banca_inicial', models.FloatField()),
                ('stopgain', models.FloatField()),
                ('stoploss', models.FloatField()),
                ('banca_atual', models.FloatField()),
                ('green', models.FloatField()),
                ('red', models.FloatField()),
                ('primeira_entrada', models.FloatField()),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('created', models.TimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
