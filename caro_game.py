import pygame 
import sys
from display import Display

pygame.init()

# Cell size = 30 and WIDTH, HEIGHT = 600, 600
 
# Player
icon_player1 = 1
icon_player2 = 2

# Player AI or HUMAN
player1 = 'human'
player2 = 'ai'

# FPS
clock = pygame.time.Clock()
FPS = 15

# Initialize display object
screen = Display()

current_type = player1
icon = icon_player1

end_turn = False

running = True
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
            pygame.quit()
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
        pygame.quit()
        break