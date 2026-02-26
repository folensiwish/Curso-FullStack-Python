from django.shortcuts import render

# Create your views here.

def home(request):
    return render (request, 'home.html')

def lista_cursos(request):
    lista_curso = [
        {'nombre':'Desarrollo Web Fullstack','img':'web.jpg'},
        {'nombre':'JavaScript Moderno (ES6+)','img':'js.png'},
        {'nombre':'Diseño UI/UX con Figma','img':'uiunix.png'},
        {'nombre':'React y Next.js Profesional','img':'react.png'},
        {'nombre':'Backend con Node.js y Express','img':'node.png'}
        ]
    return render (request, 'lista_cursos.html', context={'lista_curso':lista_curso})
'''
# Es mejor agrupar la info
cursos_data = [
    {'nombre': 'Desarrollo Web', 'url': 'about'},
    {'nombre': 'JavaScript', 'url': 'detalle_curso'},
]
return render(request, 'lista_cursos.html', {'cursos': cursos_data})
'''
'''
<a href="{% url curso.url %}" class="btn btn-primary">Ir al curso</a>
'''

def detalle_curso(request):
    return render (request, 'detalle_curso.html')

def about(request):
    data = {
        'mision': 'Transformar la educación digital en Latinoamérica.',
        'stats': [
            {'cantidad': '10k+', 'titulo': 'Alumnos'},
            {'cantidad': '50+', 'titulo': 'Cursos'},
            {'cantidad': '4.9', 'titulo': 'Valoración'}
        ]
    }
    return render(request, 'about.html', {'data': data})