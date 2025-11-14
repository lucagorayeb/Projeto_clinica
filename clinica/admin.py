from django.contrib import admin
from .models import Paciente, Consulta, Agendamento
from .form import AgendamentoForm

admin.site.register(Consulta)
admin.site.register(Paciente)
admin.site.register(Agendamento)




