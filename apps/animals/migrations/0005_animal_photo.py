# Generated by Django 3.2 on 2022-07-10 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0004_alter_specie_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='photo',
            field=models.ImageField(null=True, upload_to='files/photo', verbose_name='Foto'),
        ),
    ]
