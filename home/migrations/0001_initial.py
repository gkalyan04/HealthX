# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-04 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospitals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('address', models.TextField()),
                ('street', models.TextField()),
                ('landmark', models.TextField()),
                ('locality', models.CharField(max_length=300)),
                ('pincode', models.IntegerField()),
                ('landline_number', models.IntegerField()),
                ('latitude', models.DecimalField(decimal_places=15, max_digits=30)),
                ('longitude', models.DecimalField(decimal_places=15, max_digits=30)),
                ('altitude', models.DecimalField(decimal_places=15, max_digits=30)),
                ('facility_name', models.CharField(max_length=264)),
                ('state_name', models.CharField(max_length=50)),
                ('district_name', models.CharField(max_length=50)),
            ],
        ),
    ]
