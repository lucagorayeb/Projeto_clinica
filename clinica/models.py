from django.db import models
from .enums import SexoPaciente



    #def __str__(self):
        #return f'''nome: {self.nome}'''
    
class Endereco(models.Model):
    id_endereco = models.AutoField(primary_key=True)
    logradouro_endereco = models.CharField(max_length=100, null=False)
    numero_endereco = models.IntegerField()
    bairro_endereco = models.CharField(max_length=100, null = False)
    cep_endereco = models.CharField(max_length=16, null=False)
    cidade_endereco = models.CharField(max_length=100, null=False)
    estado_endereco = models.CharField(max_length=2, null=False)
    

    #def __str__(self):
     #   return f'''Endereço: {self.logradouro_endereco}, {self.numero_endereco}, {self.bairro_endereco}'''

class Paciente(models.Model):
    id_paciente = models.IntegerField(unique=True, auto_created=True)
    nome_paciente = models.CharField(primary_key=True,max_length=100, default='')
    cpf_paciente = models.CharField(max_length=14, default='')
    rg_paciente = models.CharField(max_length=14, default='')
    data_nascimento_paciente = models.DateField()
    sexo_paciente = models.CharField(max_length=1, choices=SexoPaciente, default=SexoPaciente.outro)
    numero_paciente = models.CharField(max_length=16)
    fk_id_endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    


    
    
