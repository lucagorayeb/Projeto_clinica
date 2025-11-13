from django.db import models
from .enums import SexoPaciente


class Paciente(models.Model):
    nome = models.CharField(primary_key=True,max_length=100, default='')
    CPF = models.CharField(max_length=14, default='')
    RG = models.CharField(max_length=14, default='')
    Data_Nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SexoPaciente, default=SexoPaciente.outro)
    contato = models.CharField(max_length=16)
    logradouro = models.CharField(max_length=100, null=False)
    lote = models.IntegerField(null=False)
    bairro = models.CharField(max_length=100, null=False)
    CEP = models.CharField(max_length=9, null=False)
    cidade = models.CharField(max_length=100, null=False)
    estado = models.CharField(max_length=2, null=False)

    def __str__(self):
        return f'{self.nome}'







    
    
