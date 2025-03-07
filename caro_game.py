import pygame 
import sys
from display import Display
from pre_enter_display import pre_enter_display

pygame.init()

# Cell size = 30 and WIDTH, HEIGHT = 600, 600

# Screen dimensions for pre-enter Screen
WIDTH, HEIGHT = 600, 400

# Define colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)
BLACK = (0, 0, 0)
 
# Player
icon_player1 = 1
icon_player2 = 2

# Player AI or HUMAN
player1 = 'human'
player2 = 'ai'

# FPS
clock = pygame.time.Clock()
FPS = 15


pre_enter_screen = pre_enter_display()
running = False

while True:
    clock.tick(5)
    pre_enter_screen.screen.fill(WHITE)
    
    # Draw title
    title_surface = pre_enter_screen.font.render("Select Game Mode", True, BLACK)
    title_rect = title_surface.get_rect(center=(WIDTH // 2, 40))
    pre_enter_screen.screen.blit(title_surface, title_rect)
    
    # Draw buttons
    pre_enter_screen.draw_button(pre_enter_screen.pvp_rect, "Player vs Player")
    pre_enter_screen.draw_button(pre_enter_screen.pvb_rect, "Player vs Bot")
    pre_enter_screen.draw_button(pre_enter_screen.bvb_rect, "Bot vs Bot")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            if pre_enter_screen.pvp_rect.collidepoint(mouse_pos):
                player1 = 'human'
                player2 = 'human'
                running = True
            elif pre_enter_screen.pvb_rect.collidepoint(mouse_pos):
                player1 = 'human'
                player2 = 'ai'
                running = True
            elif pre_enter_screen.bvb_rect.collidepoint(mouse_pos):
                player1 = 'ai'
                player2 = 'ai'
                running = True
    
    if running:
        # Initialize display object
        screen = Display()

        current_type = player1
        icon = icon_player1

        end_turn = False

        while running:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.MOUSEBUTTONDOWN and current_type == 'human': 
                    x, y = event.pos
                    if not screen.update_map(x, y, icon):
                        continue 

                    # Update player
                    if icon == icon_player1: 
                        current_type = player2
                        icon = icon_player2
                    else:
                        current_type = player1
                        icon = icon_player1
                    
                    # End turn for Ai can not print
                    end_turn = True

            if end_turn:
                screen.draw_screen()
            
                winner = screen.check_winner(3 - icon)
                
                if winner:
                    # Find the winner
                    screen.print_winner(winner)
                    pygame.time.delay(5000)
                    break

                end_turn = False
                continue

            if current_type == 'ai' and running and not end_turn:
                # Get a new move by Ai
                condition = True

                for i in range(screen.rows):
                    for j in range(screen.cols):
                        if screen.mp[i][j] == 0: 
                            # Ai choose this one.
                            screen.update_map(j * screen.cell_size, i * screen.cell_size, icon)

                            # Update player
                            if icon == icon_player1: 
                                current_type = player2
                                icon = icon_player2
                            else:
                                current_type = player1
                                icon = icon_player1 
                            
                            # Break
                            condition = False
                            break

                    if not condition:
                        break

            screen.draw_screen()
            
            winner = screen.check_winner(3 - icon)
            
            if winner:
                # Find the winner
                screen.print_winner(winner)
                pygame.time.delay(5000)
                break

        pre_enter_screen = pre_enter_display()
        running = False

    pygame.display.update() 
