from django.shortcuts import render
from DatabaseExample.forms import FormularioPrueba

def formulario(request):
    if request.method == "POST":
        form = FormularioPrueba(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            ctx = {"asunto":info['asunto'], "email":info['email'], "message": info['mensaje']}
            return render(request, "respuesta.html", ctx)
    else:
        form = FormularioPrueba()
    return render(request, "formulario.html", {"form":form})

