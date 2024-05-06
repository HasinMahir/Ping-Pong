import pygame

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 30)
title_font = pygame.font.SysFont("Arial", 100)
pygame.display.set_caption("Ping Pong")

# set up variables for the display
size = (900, 650)
screen = pygame.display.set_mode(size)

# render the text for later

# the loop will carry on until the user exits the game
run = True
game_over = False
display = False

# -------- Main Program Loop -----------
while run:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill((0, 0, 0))

    # title screen
    if not display and not game_over:
        instructions_1 = "Ping"
        instructions_1_cont = "Pong"
        instructions_2 = "Use the W and S keys for Player 1"
        instructions_3 = "Use the up and down arrow keys for Player 2"
        instructions_4 = "First to 7 points wins!"
        instructions_5 = "Click anywhere on the screen to begin!"
        display_instruction_1 = title_font.render(instructions_1, True, (255, 50, 100))
        display_instruction_1_cont = title_font.render(instructions_1_cont, True, (50, 100, 255))
        display_instruction_2 = my_font.render(instructions_2, True, (255, 255, 255))
        display_instruction_3 = my_font.render(instructions_3, True, (255, 255, 255))
        display_instruction_4 = my_font.render(instructions_4, True, (255, 255, 255))
        display_instruction_5 = my_font.render(instructions_5, True, (255, 255, 255))
        screen.blit(display_instruction_1, (250, 0))
        screen.blit(display_instruction_1_cont, (435, 0))
        screen.blit(display_instruction_2, (250, 200))
        screen.blit(display_instruction_3, (250, 250))
        screen.blit(display_instruction_4, (250, 300))
        screen.blit(display_instruction_5, (250, 350))

    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
