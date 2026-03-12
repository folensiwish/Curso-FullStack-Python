from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100,error_messages={
        'required': 'Por favor escribe tu nombre.'})
    correo = forms.EmailField(error_messages={
        'required': 'El correo es obligatorio',
        'invalid': 'Ingresa un correo válido',
    })
    mensaje = forms.CharField(widget=forms.Textarea, min_length=10,error_messages={
        'required': 'No puedes enviar un mensaje vacío',
        'min_length': 'El mensaje debe ser de al menos 10 caracteres',
    })