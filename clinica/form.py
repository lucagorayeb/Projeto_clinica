from django import forms
from django.core.exceptions import ValidationError
from .models import Paciente, Consulta, Agendamento

class AgendamentoForm(forms.Form):
    class Meta:
        model = Agendamento
        fields = ['id_agendamento', 'Data_da_Consulta', 'Tipo_da_Consulta', 'Qual_Plano', 'Carteira_do_Plano', 'Valor_da_Consulta', 'Emitiu_Nota_Fiscal', 'Queixa_do_Paciente']
        labels = {
            'Data_da_Consulta': 'Data da Consulta',
            'Tipo_da_Consulta': 'Tipo da Consulta',
            'Qual_Plano': 'Convênio',
            'Carteira_do_Plano': 'Número da carteira do convênio',
            'Valor_da_Consulta': 'Valor da Consulta',
            'Emitiu_Nota_Fiscal': 'Emitiu nota fiscal',
            'Queixa_do_Paciente': 'Queixa do paciente'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.fields['Tipo_da_Consulta'].get() == 'Particular':
            self.fields['Qual_Plano'].disabled = True
            self.fields['Carteira_do_Plano'].disabled = True