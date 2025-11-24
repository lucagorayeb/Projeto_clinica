from django.contrib import admin
from .models import Paciente, Agendamento, Consulta
from .form import AgendamentoForm, ConsultaForm


class PacienteAdmin(admin.ModelAdmin):
    list_display = [ 'nome', 'CPF']

    fieldsets = (
        ('Dados pessoais', {
            'fields': ('nome', 'CPF', 'RG', 'Data_Nascimento', 'sexo', 'contato')
        }),
        ('Endereço', {
            'fields': ('logradouro', 'lote', 'bairro', 'CEP', 'cidade', 'estado')
        }),
    )
    search_fields = ['nome']

class AgendamentoAdmin(admin.ModelAdmin):
    form = AgendamentoForm
    list_display = ['paciente_agendamento', 'Data_do_Agendamento', 'Data_da_Consulta', 'data_do_retorno']

    fieldsets = (
        ('Detalhes do Agendamento', {
            'fields': ('Data_do_Agendamento', 'Tipo_da_Consulta', 'Qual_Plano', 'Carteira_do_Plano',
                        'Data_da_Consulta', 'Valor_da_Consulta', 'Emitiu_Nota_Fiscal', 'Queixa_do_Paciente',)
        }),

        ('Paciente', {
            'fields': ('paciente_agendamento', 'data_do_retorno',)
        }),
    )
    autocomplete_fields = ['paciente_agendamento']

class ConsultaAdmin(admin.ModelAdmin):
    form = ConsultaForm
    list_display = ['paciente_consulta', 'Consulta_Realizada', 'retorno_realizado']

    fieldsets = (
        ('Detalhes da Consulta', {
            'fields': ('Consulta_Realizada','Paciente_Trouxe_Exames','Exames_Trazidos','Laudos_dos_Exames_Trazidos','achados_clinicos_da_consulta',
                        'Conduta','Encaminhado_para_Outro_Profissional','Profissional_Encaminhado','estimativa_diagnostico','exames_solicitados',)
        }),

        ('Detalhes do Retorno', {
            'fields': ('retorno_realizado','Laudos_dos_Exames_solicitados','achados_clinicos_do_retorno', 'Encaminhado_para_Outro_Profissional_retorno','Profissional_Encaminhado_retorno',
                       'confimacao_diagnostico','conduta_retorno',)
        }),

        ('Paciente', {
            'fields': ('paciente_consulta',)
        }),
    )
    autocomplete_fields = ['paciente_consulta']


admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Agendamento, AgendamentoAdmin)
admin.site.register(Consulta, ConsultaAdmin)
