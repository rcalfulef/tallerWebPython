# Generated by Django 2.2.6 on 2019-10-08 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0010_auto_20191008_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juguete',
            name='descripcion',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='juguete',
            name='imageFile',
            field=models.FileField(blank=True, null=True, upload_to='images/', verbose_name='Imagen'),
        ),
    ]