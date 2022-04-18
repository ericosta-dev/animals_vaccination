# Generated by Django 3.2 on 2022-04-05 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Specie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=30, verbose_name='Nome')),
                ('birthdate', models.DateField(verbose_name='Data de Nascimento')),
                ('specie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.specie', verbose_name='Espécie')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]