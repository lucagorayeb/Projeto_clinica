from django.db import models

class SexoPaciente:
    def  escolhe_sexo():
        paciente_sexo = {
            "M": "Masculino",
            "F": 'Feminino',
            'O': 'Outro',
        }

        return paciente_sexo

class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nome_paciente = models.CharField(max_length=100, default='')
    cpf_paciente = models.CharField(max_length=14, default='')
    rg_paciente = models.CharField(max_length=14, default='')
    data_nascimento_paciente = models.DateField()
    sexo_paciente = models.CharField(max_length=1, choices=SexoPaciente.escolhe_sexo())
    numero_paciente = models.CharField(max_length=16)

    def __str__(self):
        return f'''nome: {self.nome}'''

class Endereco(models.Model):
    id_endereco = models.AutoField(primary_key=True)
    logradouro_endereco = models.CharField(max_length=100, null=False)
    numero_endereco = models.IntegerField(null=False)
    bairro_endereco = models.CharField(max_length=100, null=False)
    cep_endereco = models.CharField(max_length=9, null=False)
    cidade_endereco = models.CharField(max_length=100, null=False)
    estado_endereco = models.CharField(max_length=2, null=False)
    fk_id_paciente = models.ForeignKey(Paciente, on_delete= models.CASCADE)

    def __str__(self):
        return f'''CEP: {self.cep_endereco}'''



    
    
