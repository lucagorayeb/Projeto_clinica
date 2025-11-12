from django.db import models

class SexoPaciente(models.TextChoices):
    masculino = 'M'
    feminino = 'F'
    outro = 'O'