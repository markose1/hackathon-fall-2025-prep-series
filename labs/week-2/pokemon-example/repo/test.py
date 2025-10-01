from client import PokeClient
from domain import Pokemon
from .pokemon_repo import PokemonRepo

pokemon_repo = PokemonRepo.instance()
pokemon_client = PokeClient()

data = pokemon_client.fetch()

for p in data:
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
    pokemon_repo.write(pokemon)

print(pokemon_repo.read_all())
