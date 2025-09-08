from django.shortcuts import render

def index(request):
    return render(request, 'app_enzocopto/index.html')

def personal(request):
    return render(request, 'app_enzocopto/personal.html')

def clientes(request):
    return render(request, 'app_enzocopto/clientes.html')

def egresados(request):
    return render(request, 'app_enzocopto/egresados.html')
