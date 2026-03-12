from django.shortcuts import render
from .forms import ContactoForm

def contacto(request):
    datos_enviados = None

    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            datos_enviados = {
                'nombre': form.cleaned_data['nombre'],
                'correo': form.cleaned_data['correo'],
                'mensaje': form.cleaned_data['mensaje'],
            }
            # Aquí podrías enviar el email, guardar en BD, etc.
            # Luego renderizas con los datos confirmados
            return render(request, 'contacto.html', {
                'form': ContactoForm(),          # form vacío para nuevo envío
                'datos_enviados': datos_enviados # datos del envío exitoso
            })
        # Si el form NO es válido, cae aquí y re-renderiza con errores
    else:
        form = ContactoForm()

    return render(request, 'contacto.html', {'form': form})
    