from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def busquedaproducto(request):
    return render(request, 'busqueda.html')

def buscar(request):

    producto = request.GET('prd')
    return HttpResponse("siuuuu")