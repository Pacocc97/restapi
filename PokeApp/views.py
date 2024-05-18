from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from .models import Pokemon
from .serializers import PokemonSerializer
from .services import PokemonApiService, ScoreService

@api_view(['GET'])
def get_pokemon_list(request):
    limit = request.GET.get('limit')
    offset = request.GET.get('offset')
    try:
        pokemon_data = PokemonApiService.get_pokemon_list(limit, offset)
        if pokemon_data:
            processed_data = PokemonApiService.process_pokemon_list(pokemon_data, limit, offset)
            return Response(processed_data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
@api_view(['GET'])
def get_pokemon_data(request, pokemon_name_or_id):
    try:
        pokemon_data = PokemonApiService.get_pokemon_data(pokemon_name_or_id)
        if pokemon_data:
            processed_data = PokemonApiService.process_pokemon_data(pokemon_data)
            return Response(processed_data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def create_pokemon(request):
    name = request.data.get('name')
    if Pokemon.objects.filter(name=name).exists():
        return Response({'error': 'Ya existe un Pokémon con ese nombre'}, status=status.HTTP_400_BAD_REQUEST)
    serializer = PokemonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT'])
def update_pokemon(request, pk):
    try:
        pokemon = Pokemon.objects.get(pk=pk)
        request.data['updated_at'] = timezone.now()
        serializer = PokemonSerializer(pokemon, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['DELETE'])
def delete_pokemon(request, pk):
    try:
        pokemon = Pokemon.objects.get(pk=pk)
        pokemon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_detailed_pokemon(request, pk):
    try:
        pokemon = Pokemon.objects.get(pk=pk)
        serializer = PokemonSerializer(pokemon)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_all_pokemon(request):
    try:
        pokemons = Pokemon.objects.all()
        total_score = sum(ScoreService.calculate_score(pokemon) for pokemon in pokemons)
        serializer = PokemonSerializer(pokemons, many=True)
        response_data = {
            "score": total_score,
            "results": serializer.data
        }
        return Response(response_data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_pokemon_score(request, pk):
    try:
        pokemon = Pokemon.objects.get(pk=pk)
        score = ScoreService.calculate_score(pokemon)
        return Response({"score": score})
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)