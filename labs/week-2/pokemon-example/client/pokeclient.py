import requests
import os
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://pokeapi.co/api/v2/")

class PokeClient:
    def fetch(self, limit: int = 100) -> List[Dict]:
        params = {
            "limit": limit
        }
        response = requests.get(url=BASE_URL, params=params)
        response.raise_for_status()
        data: Dict = response.json()
        pokemons: List[Dict] = data.get("results", [])
  
        res: List[Dict] = []
        
        for idx, pokemon in enumerate(pokemons):
            payload = {
                "id": idx,
                "name": pokemon.get("name"),
                **self._process_pokemon(pokemon.get("url"))
            }

            res.append(payload)

        return res

    def _process_pokemon(self, url: str) -> Dict:
        payload = {}

        response = requests.get(url)
        response.raise_for_status()
        data: Dict = response.json()

        payload["height"] = data.get("height")
        payload["weight"] = data.get("weight")

        types_data: List[Dict] = data.get("types")
        types = []

        for type in types_data:
            types.append(type["type"]["name"])

        payload["types"] = types

        abilities_data: List[Dict] = data.get("abilities")
        abilites = []

        for ability in abilities_data:
            abilites.append(ability["ability"]["name"])

        payload["abilities"] = abilites

        stats: List[Dict] = data.get("stats")

        for stat in stats:
            if stat["stat"]["name"]== "hp":
                payload["hp"] = stat.get("base_stat")
            elif stat["stat"]["name"] == "attack":
                payload["attack"] = stat.get("base_stat")
            elif stat["stat"]["name"] == "defense":
                payload["defense"] = stat.get("base_stat")

        return payload
    