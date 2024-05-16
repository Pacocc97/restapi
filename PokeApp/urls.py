from django.urls import path
from . import views

urlpatterns = [
    path('pokemon/select/<str:pokemon_name_or_id>/', views.get_pokemon_data, name='get-pokemon-data'),
    path('pokemon/list/', views.get_pokemon_list, name='get-pokemon-list'),
    path('pokemon/', views.create_pokemon, name='create-pokemon'),
    path('pokemon/update/<str:pk>', views.update_pokemon, name='update-pokemon'),
    path('pokemon/delete/<str:pk>/', views.delete_pokemon, name='delete-pokemon'),
    path('pokemon/detail/<str:pk>/', views.get_detailed_pokemon, name='get-detailed-pokemon'),
    path('pokemon/all/', views.get_all_pokemon, name='get-all-pokemon'),
    path('pokemon/score/<str:pk>/', views.get_pokemon_score, name='get-pokemon-score'),
]
