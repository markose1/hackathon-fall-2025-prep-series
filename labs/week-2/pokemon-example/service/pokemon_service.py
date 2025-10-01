from client import PokeClient
from domain import Pokemon
from repo import PokemonRepo
from dtos import PokemonDTO
from typing import List

class PokemonService:
    def __init__(self):
        self._client = PokeClient()
        self._repo = PokemonRepo.instance()

    def preload(self) -> None:
        raw = self._client.fetch()
        for p in raw:
            pokemon = Pokemon(
                id=p.get("id"),
                name=p.get("name"),
                height=p.get("height"),
                weight=p.get("weight"),
                types=p.get("types"),
                abilities=p.get("abilities"),
                hp=p.get("hp"),
                attack=p.get("attack"),
                defense=p.get("defense")
            )
            self._repo.write(pokemon)

    def get(self, pokemon_id: str) -> Pokemon:
        return self._repo.read(pokemon_id)
    
    def get_all(self) -> List[PokemonDTO]:
        result: List[PokemonDTO] = []
        pokemons = self._repo.read_all()

        for pokemon in pokemons:
            result.append(
                PokemonDTO(
                    id=pokemon.id,
                    name=pokemon.name,
                    types=pokemon.types
                )
            )

        return result
    
    def search(self, prefix: str) -> List[PokemonDTO]:
        prefix = prefix.lower()
        result: List[PokemonDTO] = []
        pokemons = self._repo.read_all()

        for pokemon in pokemons:
            if pokemon.name.lower().startswith(prefix):
                result.append(
                    PokemonDTO(
                        id=pokemon.id,
                        name=pokemon.name,
                        types=pokemon.types
                    )
                )

        return result
