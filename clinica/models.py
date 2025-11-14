from django.db import models
from multiselectfield import MultiSelectField
from .enums import SexoPaciente, SimOuNao, ParticularOuConvenio, PlanosDeSaude, ConsultaRealizada, Exames, ProfissionaisParaEncaminhar
    
class Consulta(models.Model):
    id_consulta = models.AutoField(primary_key=True)
    Consulta_Realizada = models.CharField(max_length=15, choices=ConsultaRealizada)
    Paciente_Trouxe_Exames = models.CharField(max_length=5, choices=SimOuNao)   
    Exames_Trazidos = MultiSelectField(choices=Exames.choices, max_length=100, blank=True)
    Laudos_dos_Exames_Trazidos = models.CharField(max_length=2000) 
    Achados_do_Primeiro_Check_UP = models.CharField(max_length=2000)
    Conduta = models.CharField(max_length=2000)
    Encaminhado_para_Outro_Profissional = models.CharField(max_length=5, choices=SimOuNao)
    Profissional_Encaminhado = models.CharField(max_length=70, choices=ProfissionaisParaEncaminhar)
    Estimativa_da_Diagnose = models.CharField(max_length=2000)


    
class Agendamento(models.Model):
    id_agendamento = models.AutoField(primary_key=True)
    Data_da_Consulta = models.DateField()
    Tipo_da_Consulta = models.CharField(max_length=15, choices=ParticularOuConvenio)
    Qual_Plano = models.CharField(max_length=15, choices=PlanosDeSaude, null=True)
    Carteira_do_Plano = models.CharField(max_length=15, null=True)
    Valor_da_Consulta = models.DecimalField(decimal_places=2, max_digits=6)
    Emitiu_Nota_Fiscal = models.CharField(max_length=5, choices=SimOuNao)
    Queixa_do_Paciente = models.CharField(max_length=2000)

class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, default='')
    CPF = models.CharField(max_length=14, default='')
    RG = models.CharField(max_length=14, default='')
    data_Nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SexoPaciente)
    contato = models.CharField(max_length=16)
    logradouro = models.CharField(max_length=100, null=False)
    lote = models.IntegerField(null=False)
    bairro = models.CharField(max_length=100, null=False)
    CEP = models.CharField(max_length=9, null=False)
    cidade = models.CharField(max_length=100, null=False)
    estado = models.CharField(max_length=2, null=False)
    fk_agendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE, null=True)
    fk_consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.nome}'
    









    
    
