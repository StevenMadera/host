# Generated by Django 4.2.6 on 2023-10-31 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cocina', '0009_rename_dificultad_receta_calificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
