from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status
from .models import Paciente
from .serializers import PacienteSerializer
import json

@api_view (['GET'])
def get_pacientes(request):
    if request.method == 'GET':
        pacientes = Paciente.objects.all()

        serializer = PacienteSerializer(pacientes, many=True)
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view (['GET', 'PUT'])
def get_paciente_by_nome(request, name):

    try:
        paciente_name = Paciente.objects.get(pk=name)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
            serializer = PacienteSerializer(paciente_name)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = PacienteSerializer(paciente_name, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def paciente_manager(request):

    if request.method == 'GET':
        try:
            if request.GET['paciente']:
                paciente_nome = request.GET['paciente']
                try:
                    paciente = Paciente.objects.get(pk=paciente_nome)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                serializer = PacienteSerializer(paciente)
                return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'POST':
        new_paciente = request.data
        serializer = PacienteSerializer(data=new_paciente)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        paciente = request.data['nome']

        try:
            update_paciente = Paciente.objects.get(pk=paciente)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        print(f'Data = {request.data}')

        serializer = PacienteSerializer(update_paciente, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        try:
            paciente_to_delete = Paciente.objects.get(pk=request.data['nome'])
            paciente_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


def home(request):
    return render(request, 'clinica/public/home.html')

def professional(request):
    return render(request, 'clinica/public/professional.html')

def desease(request):
    return render(request, 'clinica/public/desease/base_desease.html')

def about(request):
    return render(request, 'clinica/public/about.html')

def desease_cirurgia_traumatologia(request):
    return render(request, 'clinica/public/desease/cirugia_traumatologia.html')

def desease_periconarite(request):
    return render(request, 'clinica/public/desease/periconarite.html')

def desease_dentes_inclusos(request):
    return render(request, 'clinica/public/desease/dentes_inclusos.html')

def tracionamento_dentario(request):
    return render(request, 'clinica/public/desease/tracionamento_dentario.html')

def cisto_odontogenico(request):
    return render(request, 'clinica/public/desease/cisto_odontogenico.html')

def freio(request):
    return render(request, 'clinica/public/desease/freio.html')

def enxertos(request):
    return render(request, 'clinica/public/desease/enxertos.html')

def seio_maxilar(request):
    return render(request, 'clinica/public/desease/seio_maxilar.html')

def implantes(request):
    return render(request, 'clinica/public/desease/implantes.html')

def atm(request):
    return render(request, 'clinica/public/desease/atm.html')

def traumas_face(request):
    return render(request, 'clinica/public/desease/traumas_face.html')

def ortognatica(request):
    return render(request, 'clinica/public/desease/ortognatica.html')

def expansao_maxila(request):
    return render(request, 'clinica/public/desease/expansao_maxila.html')




