
from django import forms
from Aplicacion1.models import *
# Ejemplo 1:
class ClienteForm1(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'edad', 'soltero', 'descripcion', 'cumpleaños']
        widgets = {
            'cumpleaños': forms.DateInput(attrs={'type': 'date'}),
            'descripcion': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }
        
# Ejemplo 2:
class ClienteForm2(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'edad', 'soltero', 'descripcion', 'cumpleaños']

    def clean_edad(self):
        edad = self.cleaned_data.get('edad')
        if edad < 18:
            raise forms.ValidationError('La edad debe ser mayor o igual a 18 años.')
        return edad
    
# Ejemplo 3:
class ArticuloForm1(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['nombre', 'marca', 'seccion', 'precio']
        widgets = {
            'precio': forms.NumberInput(attrs={'step': 0.01}),
        }
        
# Ejemplo 4:
class BuscarArticuloForm(forms.Form):
    nombre = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'placeholder': 'Nombre del artículo'}))
    
# MANEJO SESIONES:
class InicioSesionForm(forms.Form):
    nombre = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    contraseña = forms.CharField(label='Contraseña', widget=forms.PasswordInput)