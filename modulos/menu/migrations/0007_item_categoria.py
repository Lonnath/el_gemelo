# Generated by Django 4.2.7 on 2023-11-27 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_alter_preparacion_item_alter_preparacion_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='categoria',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
