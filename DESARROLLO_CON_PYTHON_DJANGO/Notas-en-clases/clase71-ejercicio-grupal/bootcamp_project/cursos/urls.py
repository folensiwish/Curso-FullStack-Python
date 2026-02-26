from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.home, name='home'),
    path('lista_cursos/',views.lista_cursos, name='lista_cursos'),
    path('detalle_curso/',views.detalle_curso, name='detalle_curso'),
    path('about/',views.about, name='about'),
]
