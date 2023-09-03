# Generated by Django 4.2.3 on 2023-07-24 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KEMI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location_lat', models.FloatField()),
                ('location_lon', models.FloatField()),
                ('service', models.CharField(max_length=100)),
            ],
        ),
    ]