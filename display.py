# Colors
WHITE    = (255, 255, 255)
BLACK    = (0, 0, 0)
RED      = (255, 0, 0)
GREEN    = (0, 255, 0)
BLUE     = (0, 0, 255)
YELLOW   = (255, 255, 0)
CYAN     = (0, 255, 255)
MAGENTA  = (255, 0, 255)
GRAY     = (128, 128, 128)

import pygame

# Load image O
image = pygame.image.load("image/o.png") 
O_scaled_image = pygame.transform.scale(image, (20, 20))

 # Load image X
image = pygame.image.load("image/x.jpg") 
X_scaled_image = pygame.transform.scale(image, (20, 20))


class Display(): 
    def __init__(self, width = 600, height = 600, cell_size = 30):
        self.width = width
        self.height = height 
        self.cell_size = cell_size
        self.rows = self.height // cell_size
        self.cols = self.width // cell_size
        self.mp = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        # Set screen object
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("CARO")
    
    def update_map(self, x, y, icon):
        j = x // self.cell_size; i = y // self.cell_size
        
        # Check if there is another player get this move
        if self.mp[i][j] != 0:
            return False
        
        self.mp[i][j] = icon
        return True
    
    def check_winner(self, current_player: int):
        win_count = 5  # Number of consecutive marks needed to win

        # Define the four directions: (dx, dy)
        directions = [
            (0, 1),   # horizontal (to the right)
            (1, 0),   # vertical (down)
            (1, 1),   # diagonal (down-right)
            (-1, 1)   # diagonal (up-right)
        ]

        for i in range(self.rows):
            for j in range(self.cols):
                if self.mp[i][j] == 0 or self.mp[i][j] != current_player:
                    continue  # Skip empty cells and not current player

                for dx, dy in directions:
                    count = 1  # Count shells
                    x, y = i + dx, j + dy

                    while (0 <= x < self.rows and 0 <= y < self.cols and self.mp[x][y] == current_player):
                        count += 1
                        if count == win_count:
                            return current_player  # Found a winner!
                        x += dx
                        y += dy

        return None  # No winner found

    
    def print_winner(self, winner):
        font = pygame.font.SysFont(None, 48)
        
        # Text to print
        text = f"Player {winner} wins!"
        text_surface = font.render(text, True, BLACK)
        
        # Calculate the size of the window based on text size with some padding
        padding = 20
        window_width = text_surface.get_width() + padding
        window_height = text_surface.get_height() + padding
        window_rect = pygame.Rect(0, 0, window_width, window_height)
        window_rect.center = (self.width // 2, self.height // 2)
        
        # Draw a filled rectangle as the background for the winner window
        pygame.draw.rect(self.screen, YELLOW, window_rect)
        # Draw a border around the window
        pygame.draw.rect(self.screen, BLACK, window_rect, 2)
        
        # Position the text in the center of the window
        text_rect = text_surface.get_rect(center=window_rect.center)
        self.screen.blit(text_surface, text_rect)
        
        # Update display to show the window
        pygame.display.update()

    
    def draw_screen(self):
        self.screen.fill(WHITE)
        for i in range(self.rows):
            # Print lines
            pygame.draw.line(self.screen, BLACK, (0, i * self.cell_size), (self.width, i * self.cell_size), 1)

        for i in range(self.cols):
            # Print vetical lines
            pygame.draw.line(self.screen, BLACK, (i * self.cell_size, 0), (i * self.cell_size, self.height), 1)

        for i in range(self.rows):
            for j in range(self.cols):
                if self.mp[i][j] == 1:
                    # Draw X
                    x, y = j * self.cell_size + 5, i * self.cell_size + 5
                    self.screen.blit(X_scaled_image, (x, y))
                     
                elif self.mp[i][j] == 2:
                    # Draw O
                    x, y = j * self.cell_size + 5, i * self.cell_size + 5
                    self.screen.blit(O_scaled_image, (x, y))

        pygame.display.update() 