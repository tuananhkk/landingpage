# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-17 07:36
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Full Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, verbose_name='Phone Number')),
                ('content', models.TextField(max_length=150, verbose_name='Request Details')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Request Time')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
