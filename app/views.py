from django.shortcuts import render
from app.forms import CarrosForm

# Criando novas telas


def home(request):
    return render(request, 'index.html')


def form(request):
    return render(request, 'form.html', data)


def cadastro(request):
    return render(request, 'cadastro.html')
