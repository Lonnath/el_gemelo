# Generated by Django 4.2.7 on 2023-12-12 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='empleado',
        ),
        migrations.DeleteModel(
            name='DetalleVenta',
        ),
        migrations.DeleteModel(
            name='Venta',
        ),
    ]