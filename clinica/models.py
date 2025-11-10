from django.db import models

class Paciente(models.Model):
    nome = models.CharField(primary_key=True, max_length=100, default='')
    cpf = models.CharField(max_length=14, default='')
    rg = models.CharField(max_length=14, default='')
    data_nascimento = models.DateField()

    def __str__(self):
        return f'''nome: {self.nome}'''


    
    
