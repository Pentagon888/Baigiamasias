# Generated by Django 4.2.4 on 2023-08-31 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Grostena_app', '0011_remove_autoservice_repair_categories_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autoservice',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Grostena_app.repaircategory'),
        ),
    ]
