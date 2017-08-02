# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 16:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frequencia',
            name='bolsista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registros', to='vinculos.Bolsista', verbose_name='Bolsista'),
        ),
        migrations.AlterField(
            model_name='frequencia',
            name='maquina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registros', to='registro.Maquina', verbose_name='Máquina'),
        ),
    ]
