from django.urls import path
from .views import inicio,mision,vision,acerca_de # Importa la vista

urlpatterns = [
    path('inicio/', inicio, name='inicio'),  # Define la URL
    path('mision/', mision, name='mision'),
    path('vision/', vision, name='vision'),
    path('acerca-de/', acerca_de, name='acerca_de'),
]
