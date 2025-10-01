from typing import Dict, List
from domain import Pokemon

class PokemonRepo:
    _instance = None

    def __init__(self):
        self._pokemons: Dict[str, Pokemon] = {}

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = PokemonRepo()
        return cls._instance

    def write(self, p: Pokemon) -> None:
        self._pokemons[p.id] = p

    def read(self, pokeman_id: str) -> Pokemon:
        return self._pokemons.get(pokeman_id)
    
    def read_all(self) -> List[Pokemon]:
        return list(self._pokemons.values())
    