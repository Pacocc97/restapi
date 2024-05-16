import requests

class PokemonApiService:
    @staticmethod
    def get_pokemon_list(limit,offset):
        url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}"
        response = requests.get(url)
        return response.json() if response.ok else None
    
    @staticmethod
    def process_pokemon_list(pokemon_data,limit,offset):
        base_url = "http://localhost:8000/api/pokemon/list"
        processed_data = {
            "count": pokemon_data["count"],
            "next": f"{base_url}?limit={limit}&offset={int(offset) + int(limit)}",
            "previous": f"{base_url}?limit={limit}&offset={max(int(offset) - int(limit), 0)}" if offset >= limit else None,
            "results": []
        }
        
        for pokemon in pokemon_data["results"]:
            processed_pokemon = {
                "name": pokemon["name"],
                "url": f"http://localhost:5173/pokemon/{pokemon["name"]}"
            }
            processed_data["results"].append(processed_pokemon)
        
        return processed_data
  
    @staticmethod
    def get_pokemon_data(pokemon_name_or_id):
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name_or_id}"
        response = requests.get(url)
        return response.json() if response.ok else None

    @staticmethod
    def process_pokemon_data(pokemon_data):
        processed_data = {
            "name": pokemon_data["name"],
            "pokemon_id": pokemon_data["id"],
            "types": [type_data["type"]["name"] for type_data in pokemon_data["types"]],
            "abilities": [ability_data["ability"]["name"] for ability_data in pokemon_data["abilities"]],
            "base_stats": {stat_data["stat"]["name"]: stat_data["base_stat"] for stat_data in pokemon_data["stats"]},
            "height": pokemon_data["height"],
            "weight": pokemon_data["weight"],
            "sprite_url": pokemon_data["sprites"]["front_default"]
        }
        return processed_data
      
class ScoreService:
    @staticmethod
    def calculate_score(pokemon):
        weight_types = 0.4 * len(pokemon.types) 
        weight_stats = 0.3 * sum(int(value) for value in pokemon.base_stats.values())
        weight_abilities = 0.2 * len(pokemon.abilities) 
        weight_others = 0.1 * (pokemon.height + pokemon.weight)

        score = weight_types + weight_stats + weight_abilities + weight_others
        return score