from django.contrib import admin
from django.urls import path
from app.views import home, form, cadastro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('form/', form),
    path('cadastro/', cadastro),
]
