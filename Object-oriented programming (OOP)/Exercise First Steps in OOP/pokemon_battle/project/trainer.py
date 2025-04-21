from project.pokemon import Pokemon

from typing import List

class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str) -> str:
        # for p in self.pokemons:
        #     if p.name == pokemon_name:
        #         self.pokemons.remove(p)
        #         return f"You have released {pokemon_name}"

        pokemon_to_release = next((p for p in self.pokemons if p.name == pokemon_name), None)
        if pokemon_to_release:
            self.pokemons.remove(pokemon_to_release)
            return f"You have released {pokemon_name}"

        return "Pokemon is not caught"

    def trainer_data(self) -> str:
        result = [f"Pokemon Trainer {self.name}", f"Pokemon count {len(self.pokemons)}"]
        for p in self.pokemons:
            result.append(f"- {p.pokemon_details()}")

        return "\n".join(result)
    