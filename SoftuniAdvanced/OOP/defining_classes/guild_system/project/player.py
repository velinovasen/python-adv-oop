
class Player:

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        return f"Skill already added"

    def player_info(self):
        token = f"Name: {self.name}\nGuild: {self.guild}\n" \
                f"HP: {self.hp}\nMP: {self.mp}\n"
        for skill, mana in self.skills.items():
            token += f"==={skill} - {mana}" + "\n"
        return token

