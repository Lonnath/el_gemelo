# Generated by Django 4.2.7 on 2023-11-27 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_rename_compra_inventario_compraproductos_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compraproductos',
            old_name='total',
            new_name='valor_total',
        ),
        migrations.RemoveField(
            model_name='compraproductos',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='compraproductos',
            name='producto',
        ),
        migrations.AddField(
            model_name='compraproductos',
            name='referencia_compra',
            field=models.CharField(default='CI-', max_length=50, unique=True),
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('compra_inventario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.compraproductos')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.producto')),
            ],
        ),
    ]
