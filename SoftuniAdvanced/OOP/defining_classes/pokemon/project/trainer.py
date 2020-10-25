from project.pokemon import Pokemon


class Trainer:

    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon.name in [x.name for x in self.pokemon]:
            return f"This pokemon is already caught"
        self.pokemon.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        if pokemon_name in [pok.name for pok in self.pokemon]:
            pok = [p for p in self.pokemon if pokemon_name == p.name][0]
            self.pokemon.remove(pok)
            return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"

    def trainer_data(self):
        token = f"Pokemon Trainer {self.name}\n" \
                f"Pokemon count {len(self.pokemon)}\n"
        for pok in self.pokemon:
            token += "- " + pok.pokemon_details() + "\n"
        return token
