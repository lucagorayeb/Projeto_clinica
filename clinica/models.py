from django.db import models
from .enums import SexoPaciente


class Paciente(models.Model):

    id_paciente = models.IntegerField(unique=True, auto_created=True)
    nome = models.CharField(primary_key=True,max_length=100, default='')
    cPF = models.CharField(max_length=14, default='')
    rG = models.CharField(max_length=14, default='')
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SexoPaciente, default=SexoPaciente.outro)
    numero = models.CharField(max_length=16)
    logradouro = models.CharField(max_length=100, null=False)
    numero = models.IntegerField(null=False)
    bairro = models.CharField(max_length=100, null=False)
    cEP = models.CharField(max_length=9, null=False)
    cidade = models.CharField(max_length=100, null=False)
    estado = models.CharField(max_length=2, null=False)

    def __str__(self):
        return f'nome: {self.nome}'







    
    
