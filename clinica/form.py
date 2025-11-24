from django import forms
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

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta

        fields = ['id_consulta','Consulta_Realizada','Paciente_Trouxe_Exames','Exames_Trazidos','Laudos_dos_Exames_Trazidos',
                  'achados_clinicos_da_consulta','Conduta','Encaminhado_para_Outro_Profissional','Profissional_Encaminhado',
                  'estimativa_diagnostico','exames_solicitados','retorno_realizado','Laudos_dos_Exames_solicitados',
                  'achados_clinicos_do_retorno','Encaminhado_para_Outro_Profissional_retorno','Profissional_Encaminhado_retorno',
                  'confimacao_diagnostico','conduta_retorno','paciente_consulta']
        
        labels = {
            'Consulta_Realizada': 'Consulta Realizada',
            'Paciente_Trouxe_Exames': 'Paciente Trouxe Exames',
            'Exames_Trazidos': 'Exames Trazidos',
            'Laudos_dos_Exames_Trazidos': 'Laudos dos Exames Trazidos',
            'achados_clinicos_da_consulta': 'Achados Clínicos da Consulta',
            'Conduta': 'Conduta',
            'Encaminhado_para_Outro_Profissional': 'Encaminhado para Outro Profissional',
            'Profissional_Encaminhado': 'Profissional Encaminhado',
            'estimativa_diagnostico': 'Estimativa Diagnóstico',
            'exames_solicitados': 'Exames Solicitados',
            'retorno_realizado': 'Retorno Realizado',
            'Laudos_dos_Exames_solicitados': 'Laudos dos Exames Solicitados',
            'achados_clinicos_do_retorno': 'Achados Clínicos do Retorno',
            'Encaminhado_para_Outro_Profissional_retorno': 'Encaminhado para Outro Profissional no Retorno',
            'Profissional_Encaminhado_retorno': 'Profissional Encaminhado no Retorno',
            'confimacao_diagnostico': 'Confirmação Diagnóstico',
            'conduta_retorno': 'Conduta no Retorno',
            'paciente_consulta': 'Paciente',
            }
        
        widgets = {
            'Consulta_Realizada': forms.Select(),
            'Paciente_Trouxe_Exames': forms.Select(),
            'Exames_Trazidos': forms.CheckboxSelectMultiple(),
            'Laudos_dos_Exames_Trazidos': forms.Textarea(attrs={'rows':5, 'cols':50}),
            'achados_clinicos_da_consulta': forms.Textarea(attrs={'rows':5, 'cols':50}),
            'Conduta': forms.Textarea(attrs={'rows':5, 'cols':50}),
            'Encaminhado_para_Outro_Profissional': forms.Select(),
            'Profissional_Encaminhado': forms.CheckboxSelectMultiple(),
            'estimativa_diagnostico': forms.Textarea(attrs={'rows':5, 'cols':50}),
            'exames_solicitados': forms.CheckboxSelectMultiple(),
            'retorno_realizado': forms.Select(),
            'Laudos_dos_Exames_solicitados': forms.Textarea(attrs={'rows':5, 'cols':50}),
            'achados_clinicos_do_retorno': forms.Textarea(attrs={'rows':5, 'cols':50}),
            'Encaminhado_para_Outro_Profissional_retorno': forms.Select(),
            'Profissional_Encaminhado_retorno': forms.CheckboxSelectMultiple(),
            'confimacao_diagnostico': forms.Textarea(attrs={'rows':5, 'cols':50}),
            'conduta_retorno': forms.Textarea(attrs={'rows':5, 'cols':50}),
        }
        
