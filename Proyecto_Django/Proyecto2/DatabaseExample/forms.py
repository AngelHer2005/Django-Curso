from django import forms

class FormularioPrueba(forms.Form):
    asunto = forms.CharField()
    email=forms.EmailField()
    mensaje=forms.CharField()