import random

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from characters import Enemy


# Enemy types with their base stats and level scaling
# Refactor the enemy types dictionary to keep it the same
ENEMY_TYPES = {
    "Goblin": {"base_hp": 20, "hp_scale": 5, "base_attack": 5, "attack_scale": 2,
               "base_defense": 2, "defense_scale": 1, "base_xp": 15, "xp_scale": 5},
    "Orc": {"base_hp": 35, "hp_scale": 8, "base_attack": 8, "attack_scale": 3,
            "base_defense": 4, "defense_scale": 2, "base_xp": 25, "xp_scale": 8},
    "Skeleton": {"base_hp": 25, "hp_scale": 4, "base_attack": 7, "attack_scale": 2,
                 "base_defense": 1, "defense_scale": 1, "base_xp": 20, "xp_scale": 6},
    "Wolf": {"base_hp": 15, "hp_scale": 3, "base_attack": 10, "attack_scale": 3,
             "base_defense": 0, "defense_scale": 0, "base_xp": 18, "xp_scale": 4},
    "Troll": {"base_hp": 50, "hp_scale": 12, "base_attack": 12, "attack_scale": 4,
              "base_defense": 6, "defense_scale": 2, "base_xp": 35, "xp_scale": 10},
    "Dragon": {"base_hp": 100, "hp_scale": 20, "base_attack": 20, "attack_scale": 6,
               "base_defense": 12, "defense_scale": 3, "base_xp": 60, "xp_scale": 15},
    "Bandit": {"base_hp": 30, "hp_scale": 6, "base_attack": 9, "attack_scale": 3,
               "base_defense": 3, "defense_scale": 1, "base_xp": 22, "xp_scale": 7},
    "Ghost": {"base_hp": 22, "hp_scale": 5, "base_attack": 14, "attack_scale": 4,
              "base_defense": 2, "defense_scale": 0, "base_xp": 28, "xp_scale": 8},
    "Witch": {"base_hp": 28, "hp_scale": 6, "base_attack": 15, "attack_scale": 5,
              "base_defense": 3, "defense_scale": 1, "base_xp": 30, "xp_scale": 9},
    "Golem": {"base_hp": 65, "hp_scale": 15, "base_attack": 10, "attack_scale": 3,
              "base_defense": 15, "defense_scale": 4, "base_xp": 40, "xp_scale": 12},
    "Vampire": {"base_hp": 45, "hp_scale": 10, "base_attack": 16, "attack_scale": 5,
                "base_defense": 8, "defense_scale": 2, "base_xp": 38, "xp_scale": 11},
    "Werewolf": {"base_hp": 40, "hp_scale": 9, "base_attack": 18, "attack_scale": 5,
                 "base_defense": 5, "defense_scale": 2, "base_xp": 32, "xp_scale": 9},
    "Minotaur": {"base_hp": 55, "hp_scale": 13, "base_attack": 14, "attack_scale": 4,
                 "base_defense": 9, "defense_scale": 3, "base_xp": 42, "xp_scale": 12},
    "Ogre": {"base_hp": 60, "hp_scale": 14, "base_attack": 13, "attack_scale": 4,
             "base_defense": 7, "defense_scale": 2, "base_xp": 38, "xp_scale": 11},
    "Giant": {"base_hp": 80, "hp_scale": 18, "base_attack": 16, "attack_scale": 5,
              "base_defense": 10, "defense_scale": 3, "base_xp": 45, "xp_scale": 13},
    "Wraith": {"base_hp": 35, "hp_scale": 8, "base_attack": 17, "attack_scale": 5,
               "base_defense": 6, "defense_scale": 2, "base_xp": 36, "xp_scale": 10},
    "Demon": {"base_hp": 70, "hp_scale": 16, "base_attack": 19, "attack_scale": 5,
              "base_defense": 11, "defense_scale": 3, "base_xp": 50, "xp_scale": 14},
    "Cyclops": {"base_hp": 75, "hp_scale": 17, "base_attack": 15, "attack_scale": 5,
                "base_defense": 8, "defense_scale": 2, "base_xp": 43, "xp_scale": 12},
    "Phoenix": {"base_hp": 85, "hp_scale": 19, "base_attack": 18, "attack_scale": 5,
                "base_defense": 9, "defense_scale": 3, "base_xp": 55, "xp_scale": 14}
}

# Enemy name prefixes with added xp_scale
NAME_PREFIXES = [
    {"prefix": "", "xp_scale": 0},
    {"prefix": "Hungry ", "xp_scale": 1},
    {"prefix": "Fierce ", "xp_scale": 2},
    {"prefix": "Ancient ", "xp_scale": 3},
    {"prefix": "Young ", "xp_scale": -1},
    {"prefix": "Wild ", "xp_scale": 1},
    {"prefix": "Enraged ", "xp_scale": 2},
    {"prefix": "Corrupted ", "xp_scale": 3},
    {"prefix": "Savage ", "xp_scale": 2}
]

# Enemy name suffixes with added xp_scale
NAME_SUFFIXES = [
    {"suffix": "", "xp_scale": 0},
    {"suffix": " the Terrible", "xp_scale": 3},
    {"suffix": " the Weak", "xp_scale": -2},
    {"suffix": " of the Hills", "xp_scale": 1},
    {"suffix": " of the Forest", "xp_scale": 1},
    {"suffix": " the Destroyer", "xp_scale": 4},
    {"suffix": " the Hunter", "xp_scale": 2}
]


def generate_enemy(x, y, hero_level=1, enemy_level=None):

    if enemy_level is None:
        # Enemy level is randomly hero_level-2 to hero_level+2, but minimum level 1
        enemy_level = max(1, hero_level + random.randint(-2, 2))

    # Select random enemy type
    enemy_type = random.choice(list(ENEMY_TYPES.keys()))
    enemy_stats = ENEMY_TYPES[enemy_type]

    # Calculate base stats with level scaling
    hp = enemy_stats["base_hp"] + (enemy_stats["hp_scale"] * (enemy_level - 1))
    attack = enemy_stats["base_attack"] + (enemy_stats["attack_scale"] * (enemy_level - 1))
    defense = enemy_stats["base_defense"] + (enemy_stats["defense_scale"] * (enemy_level - 1))
    base_xp = enemy_stats["base_xp"] + (enemy_stats["xp_scale"] * (enemy_level - 1))

    # Generate a name with prefix and suffix
    prefix_data = random.choice(NAME_PREFIXES)
    suffix_data = random.choice(NAME_SUFFIXES)

    # Apply name modifications
    prefix = prefix_data["prefix"]
    suffix = suffix_data["suffix"]
    name_base = enemy_type
    name = f"{prefix}{name_base}{suffix}".strip()

    # Apply XP modifications from prefix and suffix
    xp_reward = max(1, base_xp + prefix_data["xp_scale"] + suffix_data["xp_scale"])

    elements = ["Fire", "Water", "Earth", "Air", "Light", "Dark"]
    element = random.choice(elements)
    possible_weaknesses = [e for e in elements if e != element]
    # Ensure weakness is explicitly a string
    weakness = str(random.choice(possible_weaknesses))

    # Calculate scale factor based on enemy vs hero level
    # This affects visual representation and can be used for additional mechanics
    scale_factor = 1.0 + (0.1 * (enemy_level - hero_level))
    scale_factor = max(0.8, min(1.5, scale_factor))  # Limit scale between 0.8 and 1.5

    # Create the enemy
    from modules.characters import Enemy
    return Enemy(
        x=x,
        y=y,
        name=name,
        level=enemy_level,  # Using the provided level instead of hardcoded 1
        hp=hp,
        xp_reward=xp_reward,
        weakness=weakness,
        attack=attack,
        defense=defense,
        scale=scale_factor,
        element=element
    )