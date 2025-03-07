import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400

# Define colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)
BLACK = (0, 0, 0)

class pre_enter_display():
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        
        self.font = pygame.font.SysFont("Arial", 24)
        # Define button dimensions and positions
        self.button_width, button_height = 250, 50
        self.pvp_rect = pygame.Rect((WIDTH - self.button_width) // 2, 80, self.button_width, button_height)
        self.pvb_rect = pygame.Rect((WIDTH - self.button_width) // 2, 160, self.button_width, button_height)
        self.bvb_rect = pygame.Rect((WIDTH - self.button_width) // 2, 240, self.button_width, button_height)

    def draw_button(self, rect, text):
        # Draw the button background and border
        pygame.draw.rect(self.screen, GRAY, rect)
        pygame.draw.rect(self.screen, DARK_GRAY, rect, 3)
        
        # Render the button text and center it
        text_surface = self.font.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)

