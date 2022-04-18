from django.db import models
from apps.accounts.behaviors import Activible
from django.contrib.auth.models import User


# Create your models here.
class Specie(Activible):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Animal(Activible):
    name = models.CharField(verbose_name='Nome',max_length=30)
    birthdate = models.DateField(verbose_name='Data de Nascimento')
    # photo = models.ImageField(verbose_name='Foto')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    specie = models.ForeignKey(Specie,on_delete=models.CASCADE,verbose_name='Espécie')
    
    def __str__(self):
        return self.name