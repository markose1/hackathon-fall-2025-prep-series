from .pokeclient import PokeClient

poke_client = PokeClient()

print(poke_client.fetch())