# Generated by Django 2.2.6 on 2019-10-08 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0009_juguete_imagefile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juguete',
            name='imageFile',
            field=models.FileField(null=True, upload_to='images/', verbose_name='Image'),
        ),
    ]
