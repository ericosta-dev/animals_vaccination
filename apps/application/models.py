from django.db import models
from apps.accounts.behaviors import Activible
from django.contrib.auth.models import User
from apps.animals.models import Animal
from apps.vaccines.models import Vaccine

# Create your models here.
class Application(Activible):
    animal = models.ForeignKey(Animal,on_delete=models.CASCADE,verbose_name='Animal')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    note = models.TextField(verbose_name='Observação',null=True, blank=True)

class VaccineApplication(Activible):
    application = models.ForeignKey(Application,on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE,verbose_name='Vacina')
    lot_number = models.CharField(max_length=30,verbose_name='Lote')
    manufacturing_date = models.DateField(verbose_name='Data de Fabricação')
    due_date = models.DateField(verbose_name='Data de Vencimento')
    notify = models.BooleanField(default=False,verbose_name='Notificação')
    notify_date = models.DateField(verbose_name='Data de Notificação',null=True, blank=True)