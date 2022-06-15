from django.forms import ModelForm
from app.models import Carros


class CarrosForm(ModelForm):
    pass


class Meta:
    model = Carros
    fields = ['modelo', 'marca', 'ano']
