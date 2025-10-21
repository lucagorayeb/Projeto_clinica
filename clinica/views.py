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


