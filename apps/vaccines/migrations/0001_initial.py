# Generated by Django 3.2 on 2022-04-25 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=30, verbose_name='Nome')),
                ('developer', models.CharField(max_length=30, verbose_name='Fabricante')),
                ('description', models.TextField()),
                ('dosage', models.CharField(max_length=10, verbose_name='Dosagem')),
                ('specie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='animals.specie', verbose_name='Especie')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
