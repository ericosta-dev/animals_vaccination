from django.db import models
from apps.accounts.behaviors import Activible
from django.contrib.auth.models import User


# Create your models here.
class Specie(Activible):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Breed(Activible):
    name = models.CharField(verbose_name='Raça', max_length=30)
    specie = models.ForeignKey(Specie,on_delete=models.CASCADE,verbose_name='Espécie')
    def __str__(self):
        breed_name = self.name + ' - ' + self.specie.name
        return breed_name

class Animal(Activible):
    name = models.CharField(verbose_name='Nome',max_length=30)
    birthdate = models.DateField(verbose_name='Data de Nascimento')
    # photo = models.ImageField(verbose_name='Foto')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    # specie = models.ForeignKey(Specie,on_delete=models.CASCADE,verbose_name='Espécie')
    breed = models.ForeignKey(Breed,on_delete=models.CASCADE,verbose_name='Raça',null=True)
    
    GENRES = (
        ('M', 'Masculino'), #Masculine
        ('F', 'Feminino'), #Feminine
    )

    gender = models.CharField(max_length=1,choices=GENRES,verbose_name='Gênero')
    
    def __str__(self):
        return self.name
