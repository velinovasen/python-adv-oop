from project.player import Player


class Guild:

    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild in [x.guild for x in self.players if player.name == x.name]:
            return f"Player {player.name} is already in the guild."
        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        player.guild = f"{self.name}"
        self.players.append(player)
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        if player_name not in [x.name for x in self.players]:
            return f"Player {player_name} is not in the guild."
        player = [x for x in self.players if x.name == player_name][0]
        player.guild = "Unaffiliated"
        self.players.remove(player)
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        token = f"Guild: {self.name}\n"
        for player in self.players:
            token += player.player_info()
        return token

