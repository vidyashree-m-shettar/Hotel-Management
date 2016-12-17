# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 13:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0004_auto_20161127_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cost', models.IntegerField()),
                ('menu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelapp.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Sweets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cost', models.IntegerField()),
                ('menu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelapp.Menu')),
            ],
        ),
        migrations.RenameModel(
            old_name='Starter',
            new_name='Bevages',
        ),
    ]