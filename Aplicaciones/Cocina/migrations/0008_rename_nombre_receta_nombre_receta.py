# Generated by Django 4.2.6 on 2023-10-31 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cocina', '0007_rename_codigo_receta_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receta',
            old_name='nombre',
            new_name='nombre_receta',
        ),
    ]