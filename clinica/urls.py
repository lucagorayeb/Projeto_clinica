from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='clinica-home'),
    path('about/', views.about, name='clinica-about'),
    path('professional/', views.professional , name='clinica-professional'),
    path('desease/', views.desease, name='clinica-desease'),
    path('desease/cirurgia-traumatologia', views.desease_cirurgia_traumatologia, name='clinica-desease-cirurgia-traumatologia'),
    path('desease/periconarite', views.desease_periconarite, name='clinica-desease-periconarite'),
    path('desease/dentes_inclusos', views.desease_dentes_inclusos, name='clinica-dentes-inclusos'),
]