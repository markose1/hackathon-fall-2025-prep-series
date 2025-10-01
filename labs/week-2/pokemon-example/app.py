from flask import Flask, request, jsonify
from dtos import PokemonDTO
from service import PokemonService
from typing import Dict, List

app = Flask(__name__)
service = PokemonService()
service.preload()

@app.get("/pokemon")
def all_pokemon():
    result: List[Dict] = []
    data: List[PokemonDTO] = service.get_all()
    
    for p in data:
        result.append(p.__dict__)

    print(result)

    return jsonify(result), 200

@app.get("/pokemon/<int:pokemon_id>")
def pokemon_detail(pokemon_id: int):
    p = service.get(pokemon_id)
    if not p:
        return jsonify({"error": "not found"}), 404
    return jsonify(p.__dict__), 200

@app.get("/pokemon/search")
def search_pokemon():
    q = request.args.get("q", "").strip()
    if not q:
        return jsonify({"error": "missing query param q"}), 400
    
    result: List[Dict] = []
    data: List[PokemonDTO] = service.search(q)
    
    for p in data:
        result.append(p.__dict__)

    return jsonify(result), 200
