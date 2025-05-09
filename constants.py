# Constants for the game
import pygame

# Screen settings
PANEL = 150
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600 + PANEL

# Game states
TITLE_SCREEN = 0
ADVENTURE_MENU = 1
GAMEPLAY = 2

# Button Colors
BUTTON_NORMAL = (120, 120, 120)
BUTTON_HOVER = (200, 200, 200)
BUTTON_TEXT = (255, 255, 255)

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)


# Messages
MAX_MESSAGES = 5

# Animation
ANIMATION_SPEED = 0.2  # Adjust as needed

# Elements
ELEMENTS = ["FIRE", "ICE", "WIND", "WATER", "NEUTRAL"]

# Define elemental weaknesses (element: [weak against])
ELEMENT_WEAKNESSES = {
    "FIRE": ["WATER", "ICE"],
    "ICE": ["FIRE", "WIND"],
    "WIND": ["ICE", "WATER"],
    "WATER": ["WIND", "FIRE"],
    "NEUTRAL": []  # Neutral has no specific weaknesses
}
# Damage multipliers
WEAKNESS_MULTIPLIER = 2.0  # Double damage when hitting weakness
RESISTANCE_MULTIPLIER = 0.5  # Half damage when hitting resistance