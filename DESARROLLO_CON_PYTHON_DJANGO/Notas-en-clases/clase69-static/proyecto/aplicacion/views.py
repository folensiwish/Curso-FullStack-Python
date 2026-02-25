from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

def login(request):
    ejercicio = 'pull up'
    sets = 3
    reps = 3
    ejercicios = ['Dominadas','Dips','Sentadillas','Muscle up']
    return render(request, 'login.html', context={
        'ejercicio':ejercicio,
        'sets':sets,
        'reps':reps,
        'ejercicios':ejercicios,
    })
