from dataclasses import dataclass
from typing import List 

@dataclass
class PokemonDTO:
    id: int
    name: str
    types: List[str]
