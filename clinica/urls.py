from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='clinica-home'),
    path('about/', views.about, name='clinica-about'),
    path('professional/', views.professional , name='clinica-professional'),
    path('desease/', views.desease, name='clinica-desease'),
    path('desease/cirurgia-traumatologia', views.desease, name='clinica-desease-cirurgia-traumatologia'),
]