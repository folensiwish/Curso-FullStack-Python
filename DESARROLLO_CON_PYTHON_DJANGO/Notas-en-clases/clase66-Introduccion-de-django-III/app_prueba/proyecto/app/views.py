from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def mensaje(request):
    return HttpResponse('Este es el mensaje de Alberto Fernandez')