from django.shortcuts import render

# Create your views here.

CARTELERA = {
    "The Matrix": {
        "genero": "Ciencia Ficción",
        "puntuacion": 8.7,
        "director": "Hermanas Wachowski"
    },
    "Knives Out": {
        "genero": "Misterio",
        "puntuacion": 7.9,
        "director": "Rian Johnson"
    },
    "Whiplash": {
        "genero": "Drama Musical",
        "puntuacion": 8.5,
        "director": "Damien Chazelle"
    },
    "Spider-Man: Into the Spider-Verse": {
        "genero": "Animación",
        "puntuacion": 8.4,
        "director": "P. Persichetti, R. Rothman, R. Ramsey"
    },
    "Parasite": {
        "genero": "Thriller",
        "puntuacion": 8.5,
        "director": "Bong Joon-ho"
    }
}

def home(request):
    return render (request, 'home.html',context={'cartelera':CARTELERA})

def perfil(request):
    nombre = request.GET['nombre_movie']
    indice = CARTELERA[nombre]
    return render(request, 'perfil.html',context={'indice':indice})