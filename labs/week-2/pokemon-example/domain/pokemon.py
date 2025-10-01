from dataclasses import dataclass
from typing import List

@dataclass
class Pokemon:
    id: int
    name: str
    height: int
    weight: int
    types: List[str]
    abilities: List[str]
    hp: int
    attack: int
    defense: int
