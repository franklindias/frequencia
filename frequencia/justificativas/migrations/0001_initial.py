# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-28 17:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vinculos', '0002_auto_20170824_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='JustificativaFalta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Registrado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('status', models.IntegerField(choices=[(0, 'Pendente'), (1, 'Indeferida'), (2, 'Deferida')], default=0, verbose_name='Status da justificativa')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('inicio', models.DateField(verbose_name='Data de início')),
                ('termino', models.DateField(verbose_name='Data de término')),
            ],
            options={
                'verbose_name_plural': 'Justificativas de falta',
                'verbose_name': 'Justificativa de falta',
            },
        ),
        migrations.CreateModel(
            name='TipoJustificativaFalta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Registrado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('nome', models.CharField(max_length=100, verbose_name='Tipo')),
            ],
            options={
                'verbose_name_plural': 'Tipos de justificativa',
                'verbose_name': 'Tipo de justificativa',
            },
        ),
        migrations.AddField(
            model_name='justificativafalta',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='justificativas', to='justificativas.TipoJustificativaFalta', verbose_name='Tipo de justificativa'),
        ),
        migrations.AddField(
            model_name='justificativafalta',
            name='vinculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='justificativas', to='vinculos.Vinculo', verbose_name='Vínculo'),
        ),
    ]
