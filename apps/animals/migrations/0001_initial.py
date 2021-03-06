# Generated by Django 3.2 on 2022-04-25 20:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=30, verbose_name='Raça')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Specie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
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
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=30, verbose_name='Nome')),
                ('birthdate', models.DateField(verbose_name='Data de Nascimento')),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, verbose_name='Gênero')),
                ('breed', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='animals.breed', verbose_name='Raça')),
                ('specie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.specie', verbose_name='Espécie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
