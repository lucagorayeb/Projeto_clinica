from django import forms
from django.core.exceptions import ValidationError
from .models import Paciente, Consulta, Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento

        fields = ['id_agendamento','Data_do_Agendamento', 'Data_da_Consulta', 'Tipo_da_Consulta', 'Qual_Plano',
                   'Carteira_do_Plano', 'Valor_da_Consulta', 'Emitiu_Nota_Fiscal', 'Queixa_do_Paciente', 'data_do_retorno', 'paciente_agendamento']
        
        labels = {
            'Data_do_Agendamento': 'Data do Agendamento',
            'Data_da_Consulta': 'Data da Consulta',
            'Tipo_da_Consulta': 'Tipo da Consulta',
            'Qual_Plano': 'Convênio',
            'Carteira_do_Plano': 'Número da carteira do convênio',
            'Valor_da_Consulta': 'Valor da Consulta',
            'Emitiu_Nota_Fiscal': 'Emitiu nota fiscal',
            'Queixa_do_Paciente': 'Queixa do paciente',
            'data_do_retorno': 'Data do Retorno',
            'paciente_agendamento': 'Paciente',
            }
        
        widgets = {
            'Data_do_Agendamento': forms.DateInput(attrs={'type': 'date'}),
            'Data_da_Consulta': forms.DateInput(attrs={'type': 'date'}),
            'Tipo_da_Consulta': forms.Select(),
            'Qual_Plano': forms.Select(),
            'Carteira_do_Plano': forms.TextInput(attrs={'maxlength': '15'}), 
            'Valor_da_Consulta': forms.NumberInput(attrs={'step': '50.00'}),
            'Emitiu_Nota_Fiscal': forms.Select(),
            'Queixa_do_Paciente': forms.Textarea(attrs={'rows':5, 'cols':50}),
            'data_do_retorno': forms.DateInput(attrs={'type': 'date'}),
        }
        
