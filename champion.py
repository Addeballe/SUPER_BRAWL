class Gladiator:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.stamina = 100
        self.attack = 0
        self.defence = 0

    def take_damage(self, damage):
        self.health -= (damage - self.self.defence)