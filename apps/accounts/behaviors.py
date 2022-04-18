from cProfile import label
from django.db import models

class Activible(models.Model):
    active = models.BooleanField(default=True,verbose_name='Ativo')
    add_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True