from django.urls import path
from . import views

urlpatterns = [
    path('types/', views.get_pokemon_types, name='get_pokemon_types'),
    path('pokemon/<str:type_name>/', views.get_pokemon_by_type, name='get_pokemon_by_type'),
    path('pokemon/details/<str:pokemon_name>/', views.get_pokemon_details, name='get_pokemon_details'),
]
