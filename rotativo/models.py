from django.db import models

class Rotativo(models.Model):
    data = models.DateField()

    def __str__(self):
        return str(self.data)
    
    hora_entrada = models.TimeField()

    def __str__(self):
        return str(self.hora_entrada)
    
    hora_saida = models.TimeField()

    def __str__(self):
        return str(self.hora_saida)
