from django.shortcuts import render

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


