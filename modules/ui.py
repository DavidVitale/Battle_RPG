import pygame

from constants import BUTTON_NORMAL, BUTTON_HOVER, BUTTON_TEXT


class Button:
    def __init__(self, x, y, width, height, text, font, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.action = action
        self.normal_color = BUTTON_NORMAL
        self.hover_color = BUTTON_HOVER
        self.text_color = BUTTON_TEXT
        self.hovered = False

    def update(self, mouse_pos):
        self.hovered = self.rect.collidepoint(mouse_pos)

    def draw(self, screen):
        color = self.hover_color if self.hovered else self.normal_color
        pygame.draw.rect(screen, color, self.rect, border_radius=12)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2, border_radius=12)

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.hovered:
            if self.action:
                return self.action()
        return None


def draw_stat_panel(screen, hero, enemy, stat_panel_img, font):
    # Draw the stat panel
    panel_rect = stat_panel_img.get_rect(topleft=(0, 600))
    screen.blit(stat_panel_img, panel_rect)

    # Draw hero stats
    hero_stats = [
        f"Level: {hero.level}",
        f"HP: {hero.hp}/{hero.max_hp}",
        f"Attack: {hero.attack}",
        f"Defense: {hero.defense}",
        f"Gold: {hero.gold}",
        f"XP: {hero.experience}"
    ]

    # Draw enemy stats
    enemy_stats = [
        f"Level: {enemy.level}",
        f"HP: {enemy.hp}/{enemy.max_hp}",
        f"Attack: {enemy.attack}",
        f"Defense: {enemy.defense}",
        f"Weakness: {enemy.weakness}"
    ]

    y_offset = 30
    for line in hero_stats:
        text_surface = font.render(line, True, (255, 255, 255))
        text_rect = text_surface.get_rect(topleft=(30, y_offset))
        screen.blit(text_surface, text_rect)
        y_offset += 30

    y_offset = 30
    for line in enemy_stats:
        text_surface = font.render(line, True, (255, 255, 255))
        text_rect = text_surface.get_rect(topleft=(600, y_offset))
        screen.blit(text_surface, text_rect)
        y_offset += 30


def draw_message_panel(screen, messages, font, x, y, width, height):
    panel = pygame.Surface((width, height), pygame.SRCALPHA)
    panel.fill((0, 0, 0, 150))
    screen.blit(panel, (x, y))

    y_offset = 10
    for message in messages:
        text_surface = font.render(message, True, (255, 255, 255))
        text_rect = text_surface.get_rect(topleft=(x + 10, y + y_offset))
        screen.blit(text_surface, text_rect)
        y_offset += 25