from .pokemon_service import PokemonService

pokemon_svc = PokemonService()
pokemon_svc.preload()
print(pokemon_svc.get_all())
print(pokemon_svc.search("b"))