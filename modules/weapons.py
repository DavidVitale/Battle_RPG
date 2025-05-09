import random


class Weapon:
    def __init__(self, name, damage, element=None,  attack_speed=1.0, durability=100):
        self.name = name
        self.damage = damage
        self.element = element
        self.attack_speed = attack_speed
        self.durability = durability
        self.max_durability = durability

    def __str__(self):
        return f"{self.name} ({self.element} element) - Damage: {self.damage}"

    def attack(self, target):
        """Attack a target with this weapon"""
        damage, was_weakness = target.take_damage(self.damage, self.element)
        # Reduce durability slightly with each use
        self.durability = max(0, self.durability - 1)
        return damage, was_weakness

    def is_broken(self):
        """Check if the weapon is broken"""
        return self.durability <= 0

    def repair(self, amount=None):
        """Repair the weapon"""
        if amount:
            self.durability = min(self.max_durability, self.durability + amount)
        else:
            self.durability = self.max_durability

def generate_weapon(tier=1):
    weapon_types = {
        "Sword": {"base_damage": 10, "speed": 1.0, "durability": 100},
        "Axe": {"base_damage": 15, "speed": 0.7, "durability": 80},
        "Dagger": {"base_damage": 7, "speed": 1.5, "durability": 60},
        "Hammer": {"base_damage": 18, "speed": 0.6, "durability": 120},
        "Spear": {"base_damage": 12, "speed": 1.2, "durability": 90},
    }

    # Prefixes for weapon names
    prefixes = ["Rusty", "Sharp", "Ancient", "Gleaming", "Cursed", "Blessed", "Mighty"]

    # Select random weapon type
    weapon_type = random.choice(list(weapon_types.keys()))
    weapon_data = weapon_types[weapon_type]

    # Scale damage based on tier
    damage = int(weapon_data["base_damage"] * (1 + (tier - 1) * 0.5))

    # Select random element (excluding NEUTRAL for higher tiers)
    available_elements = ["NEUTRAL", "FIRE", "ICE", "WIND", "WATER"]
    if tier > 1:
        # Higher tier weapons are more likely to have an element
        available_elements = ["FIRE", "ICE", "WIND", "WATER"] * 2 + ["NEUTRAL"]

    element = random.choice(available_elements)

    # Generate name
    if element != "NEUTRAL" and random.random() > 0.3:
        name = f"{random.choice(prefixes)} {element.capitalize()} {weapon_type}"
    else:
        name = f"{random.choice(prefixes)} {weapon_type}"

    # Create and return the weapon
    return Weapon(
        name=name,
        damage=damage,
        element=element,
        attack_speed=weapon_data["speed"],
        durability=weapon_data["durability"] * tier
    )

class Inventory:

    def __init__(self, max_size=5):
        self.items = []
        self.max_size = max_size

    def add_item(self, item):
        """Add an item to the inventory"""
        if len(self.items) < self.max_size:
            self.items.append(item)
            return True
        return False  # Inventory is full

    def remove_item(self, item):
        """Remove an item from the inventory"""
        if item in self.items:
            self.items.remove(item)
            return True
        return False  # Item not found

    def list_items(self):
        """List all items in the inventory"""
        if not self.items:
            return "Inventory is empty"

        result = []
        for i, item in enumerate(self.items):
            result.append(f"{i + 1}. {item}")
        return "\n".join(result)

    def get_item(self, index):
        """Get item by index"""
        if 0 <= index < len(self.items):
            return self.items[index]
        return None

    def is_full(self):
        """Check if inventory is full"""
        return len(self.items) >= self.max_size

    def __len__(self):
        return len(self.items)