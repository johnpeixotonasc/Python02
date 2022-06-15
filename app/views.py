from django.shortcuts import render
from app.forms import CarrosForm

# Create your views here


def home(request):
    return render(request, 'index.html')


def form(request):
    data = {'form': CarrosForm()}
    return render(request, 'form.html', data)


def cadastro(request):
    return render(request, 'cadastro.html')
