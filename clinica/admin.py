from django.contrib import admin
from .models import Paciente, Agendamento, Consulta


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

class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ['paciente_agendamento', 'Data_do_Agendamento', 'Data_da_Consulta']

    fieldsets = (
        ('Detalhes do Agendamento', {
            'fields': ('Data_do_Agendamento', 'Tipo_da_Consulta', 'Qual_Plano', 'Carteira_do_Plano',
                        'Data_da_Consulta', 'Valor_da_Consulta', 'Emitiu_Nota_Fiscal', 'Queixa_do_Paciente',
                        'paciente_agendamento')
        }),
    )

class ConsultaAdmin(admin.ModelAdmin):
    list_display = ['Consulta_Realizada', 'paciente_consulta']

    fieldsets = (
        ('Detalhes da Consulta', {
            'fields': ('Consulta_Realizada', 'Paciente_Trouxe_Exames', 'Exames_Trazidos',
                        'Laudos_dos_Exames_Trazidos', 'Achados_do_Primeiro_Check_UP', 'Conduta',
                        'Encaminhado_para_Outro_Profissional', 'Profissional_Encaminhado',
                        'Estimativa_da_Diagnose', 'paciente_consulta')
        }),
    )


admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Agendamento, AgendamentoAdmin)
admin.site.register(Consulta, ConsultaAdmin)
