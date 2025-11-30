from django.urls import path
from . import views
from .autocomplete import PacienteAutocomplete

urlpatterns = [
    path('', views.home, name='clinica-home'),

    path('about/', views.about, name='clinica-about'),

    path('professional/', views.professional , name='clinica-professional'),

    path('desease/', views.desease, name='clinica-desease'),

    path('desease/cirurgia-traumatologia', views.desease_cirurgia_traumatologia, name='clinica-desease-cirurgia-traumatologia'),

    path('desease/periconarite', views.desease_periconarite, name='clinica-desease-periconarite'),

    path('desease/dentes_inclusos', views.desease_dentes_inclusos, name='clinica-dentes-inclusos'),

    path('desease/tracionamento_dentario', views.tracionamento_dentario, name='clinica-tracionamento-dentario'),

    path('desease/cisto_odontogenico', views.cisto_odontogenico, name='clinica-cisto-odontogenico'),

    path('desease/freio', views.freio, name='clinica-freio'),

    path('desease/enxertos', views.enxertos, name='clinica-enxertos'),

    path('desease/seio_maxilar', views.seio_maxilar, name='clinica-seio-maxilar'),

    path('desease/implantes', views.implantes, name='clinica-implantes'),

    path('desease/atm', views.atm, name='clinica-atm'),

    path("paciente-autocomplete/", PacienteAutocomplete.as_view(), name="paciente-autocomplete"),
]