# Generated by Django 4.2.7 on 2023-11-26 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preparacion',
            old_name='materia_prima',
            new_name='producto',
        ),
    ]
