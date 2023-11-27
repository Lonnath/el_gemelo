# Generated by Django 4.2.7 on 2023-11-26 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0003_alter_proveedor_correo'),
        ('menu', '0002_rename_materia_prima_preparacion_producto'),
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='compra_inventario',
            new_name='CompraProductos',
        ),
        migrations.RenameModel(
            old_name='materia_prima',
            new_name='Producto',
        ),
        migrations.RenameField(
            model_name='compraproductos',
            old_name='materia_prima',
            new_name='producto',
        ),
        migrations.AlterModelTable(
            name='compraproductos',
            table='compras_productos',
        ),
        migrations.AlterModelTable(
            name='producto',
            table='producto',
        ),
    ]
