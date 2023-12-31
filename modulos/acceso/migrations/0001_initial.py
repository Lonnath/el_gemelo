# Generated by Django 4.2.7 on 2023-12-12 07:21

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
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True)),
                ('numero_telefono', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=254)),
                ('pais', models.CharField(max_length=100)),
                ('codigo_postal', models.CharField(max_length=10)),
                ('ciudad', models.CharField(max_length=100)),
                ('direccion', models.TextField()),
                ('fecha_edicion', models.DateTimeField(auto_now=True)),
                ('usuario', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'empleados',
            },
        ),
        migrations.CreateModel(
            name='Bloqueos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intentos', models.IntegerField(default=0)),
                ('bloqueo', models.BooleanField(default=False)),
                ('fecha_edicion', models.DateTimeField(auto_now=True)),
                ('credenciales', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'bloqueos',
            },
        ),
    ]
