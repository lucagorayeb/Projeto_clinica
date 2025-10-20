from django.shortcuts import render

def home(request):
    return render(request, 'clinica/public/home.html')

def professional(request):
    return render(request, 'clinica/public/professional.html')

def desease(request):
    return render(request, 'clinica/public/desease/base_desease.html')

def about(request):
    return render(request, 'clinica/public/about.html')
