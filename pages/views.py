from django.shortcuts import render

def home(request):
    contexto = {
        "mensagem": "Servidor ligado e respondendo."
    }
    return render(request, "pages/home.html", contexto)