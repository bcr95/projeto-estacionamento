from django.db import models

# Create your models here.
class Reserva(models.Model):
    data = models.DateField()

    def __str__(self):
        return str(self.data)
    
    hora_entrada = models.TimeField(default='00:00')

    def __str__(self):
        return str(self.hora_entrada)
    
    hora_saida = models.TimeField(default='00:00')

    def __str__(self):
        return str(self.hora_saida)
    

    