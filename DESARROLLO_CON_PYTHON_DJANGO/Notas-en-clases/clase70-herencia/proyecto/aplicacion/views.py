from django.shortcuts import render
# Create your views here.

def home(request):
    lista = ['Hola','Adios']
    return render(request,'home.html',context={
        'lista':lista
    })
