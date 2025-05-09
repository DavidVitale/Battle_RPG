from constants import WEAKNESS_MULTIPLIER


class Hero:
    def __init__(self, x, y, name, level=1, hp=100, attack=10, defense=5, scale=1.0):
        self.x = x
        self.y = y
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        self.level = level
        self.experience = 0
        self.gold = 0
        self.scale = scale
        # Add other attributes as needed

    def update(self):
        # Update logic
        pass

    def take_damage(self, amount):
        actual_damage = max(0, amount - self.defense)
        self.hp = max(0, self.hp - actual_damage)
        return actual_damage

    def is_alive(self):
        return self.hp > 0

    def gain_experience(self, amount):
        self.experience += amount
        # Level up logic

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)


class Enemy:
    def __init__(self, x, y, name, level, attack, defense, xp_reward, weakness, element, hp=50, scale=1.0):
        self.x = x
        self.y = y
        self.name = name
        self.level = level
        self.attack = attack
        self.defense = defense
        self.xp_reward = xp_reward
        self.weakness = weakness
        self.element = element
        self.hp = hp
        self.max_hp = hp
        self.scale = scale
        # Add other attributes as needed



    def update(self):
        # Update logic
        pass

    def take_damage(self, amount, attack_element="NEUTRAL"):
        damage_multiplier = 1.0

        if attack_element in self.weakness:
            damage_multiplier = WEAKNESS_MULTIPLIER

        actual_damage = max(0, int((amount - self.defense) * damage_multiplier))
        self.hp = max(0, self.hp - actual_damage)

        return actual_damage, damage_multiplier > 1.0

    def is_alive(self):
        return self.hp > 0