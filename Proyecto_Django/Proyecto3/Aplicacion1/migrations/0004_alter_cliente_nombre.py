# Generated by Django 5.0.4 on 2024-05-16 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion1', '0003_alter_cliente_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=20, verbose_name='El nombre'),
        ),
    ]
