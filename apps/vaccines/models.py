from django.db import models
from apps.accounts.behaviors import Activible
from apps.animals.models import Specie

# Create your models here.
class Vaccine(Activible):
    name = models.CharField(max_length=30,verbose_name='Nome')
    developer = models.CharField(max_length=30,verbose_name='Fabricante')
    specie = models.ForeignKey(Specie,on_delete=models.PROTECT,verbose_name='Especie')
    description = models.TextField(verbose_name='Descrição')
    dosage = models.CharField(max_length=10,verbose_name='Dosagem')
    def __str__(self):
        return self.name

# class VaccineSettings(Activible):
#     vaccine = models.ForeignKey(Vaccine,on_delete=models.PROTECT,verbose_name='Vacina')
#     TIME_TYPES = (
#         ('D', 'Dia'), #Day
#         ('M', 'Mês'), #Month
#         ('A', 'Ano'), #Year
#     )
#     # time_type = models.CharField(max_length=1,choices=TIME_TYPES,verbose_name='Tipo Tempo')
#     # time_value = models.IntegerField(verbose_name='Tempo')
#     # doses = models.IntegerField(verbose_name='Doses')

#     def __str__(self):
#         name = self.vaccine.name + " - " + self.specie.name
#         return name