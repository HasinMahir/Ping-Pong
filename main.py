import pygame
from ball import Ball
from player import Player

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 30)
title_font = pygame.font.SysFont("Arial", 100)
score_font = pygame.font.SysFont("Times New Roman", 100)
win_font = pygame.font.SysFont("Arial", 50)
pygame.display.set_caption("Pong")

# set up variables
size = (900, 650)
screen = pygame.display.set_mode(size)
ball = Ball(430, 300)
player1 = Player(0, 250)
player2 = Player(889, 250)
bg = pygame.image.load("line.png")
# game numbers
x_delta = ""
y_delta = ""
player1_score = 0
player2_score = 0
display_player1_score = score_font.render(str(player1_score), True, (50, 100, 255))
display_player2_score = score_font.render(str(player2_score), True, (255, 50, 100))

# displaying ball speed options
easy_speed = "EASY"
display_easy_speed = my_font.render(easy_speed, True, (0, 255, 0))
medium_speed = "MEDIUM"
display_medium_speed = my_font.render(medium_speed, True, (0, 0, 255))
hard_speed = "HARD"
display_hard_speed = my_font.render(hard_speed, True, (255, 0, 0))
display_easy_speed_rect = pygame.Rect(225, 500, display_easy_speed.get_rect().width, display_easy_speed.get_rect().height)
display_medium_speed_rect = pygame.Rect(425, 500, display_medium_speed.get_rect().width, display_medium_speed.get_rect().height)
display_hard_speed_rect = pygame.Rect(625, 500, display_hard_speed.get_rect().width, display_hard_speed.get_rect().height)

# the loop will carry on until the user exits the game
run = True
game_over = False
display = False
choose_speed = False
counter = 0
player1_win = False
player2_win = False

# -------- Main Program Loop -----------
while run:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

        # start the game by clicking on one of the difficulty options
        if event.type == pygame.MOUSEBUTTONUP:
            # check which option the user chooses
            if event.button == 1 and counter == 0:
                position = pygame.mouse.get_pos()
                # easy speed option
                if display_easy_speed_rect.collidepoint(position):
                    display = True
                    choose_speed = True
                    counter = counter + 1
                    x_delta = 1
                    y_delta = 1
                # medium speed option
                if display_medium_speed_rect.collidepoint(position):
                    display = True
                    choose_speed = True
                    counter = counter + 1
                    x_delta = 2
                    y_delta = 2
                # hard speed option
                if display_hard_speed_rect.collidepoint(position):
                    display = True
                    choose_speed = True
                    counter = counter + 1
                    x_delta = 3
                    y_delta = 3

        # play again
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_over:
                # reset variables
                game_over = False
                display = False
                player1_win = False
                player2_win = False
                counter = 0
                player1_score = 0
                player2_score = 0
                display_player1_score = score_font.render(str(player1_score), True, (50, 100, 255))
                display_player2_score = score_font.render(str(player2_score), True, (255, 50, 100))
                # FIX PLAY AGAIN SCREEN
                screen.blit(display_easy_speed, (225, 500))
                screen.blit(display_medium_speed, (425, 500))
                screen.blit(display_hard_speed, (625, 500))

    # background
    screen.fill((0, 0, 0))

    # title screen
    if not display and not game_over:
        instructions_1 = "Po"
        instructions_1_cont = "ng"
        instructions_2 = "Use the W and S keys for Player 1"
        instructions_3 = "Use the up and down arrow keys for Player 2"
        instructions_4 = "First to 7 points wins!"
        instructions_5 = "Choose one of the difficulty options for the ball speed to begin!"
        display_instruction_1 = title_font.render(instructions_1, True, (50, 100, 255))
        display_instruction_1_cont = title_font.render(instructions_1_cont, True, (255, 50, 100))
        display_instruction_2 = my_font.render(instructions_2, True, (255, 255, 255))
        display_instruction_3 = my_font.render(instructions_3, True, (255, 255, 255))
        display_instruction_4 = my_font.render(instructions_4, True, (255, 255, 255))
        display_instruction_5 = my_font.render(instructions_5, True, (255, 255, 255))
        screen.blit(display_instruction_1, (350, 0))
        screen.blit(display_instruction_1_cont, (450, 0))
        screen.blit(display_instruction_2, (170, 200))
        screen.blit(display_instruction_3, (170, 250))
        screen.blit(display_instruction_4, (170, 300))
        screen.blit(display_instruction_5, (170, 350))

    # choose the speed of the ball
    if not display and not choose_speed and not game_over:
        screen.blit(display_easy_speed, (225, 500))
        screen.blit(display_medium_speed, (425, 500))
        screen.blit(display_hard_speed, (625, 500))

    # when game is running
    if display and choose_speed and not game_over:
        screen.blit(bg, (0, 0))
        pygame.draw.ellipse(screen, (255, 255, 255), ball.rect)
        # move the ball by adding the delta to its x and y position
        ball.x = ball.x + x_delta
        ball.y = ball.y + y_delta
        ball.move()
        screen.blit(player1.image, player1.rect)
        screen.blit(player2.image, player2.rect)
        # if the ball hits the wall, make it bounce by inverting the x and y deltas
        if ball.x >= 870:
            x_delta = x_delta * -1
            # set the ball back to the middle of the screen
            ball.x = 430
            ball.y = 300
            player1_score = player1_score + 1
            display_player1_score = score_font.render(str(player1_score), True, (50, 100, 255))

        if ball.x <= 0:
            x_delta = x_delta * -1
            # set the ball back to the middle of the screen
            ball.x = 430
            ball.y = 300
            player2_score = player2_score + 1
            display_player2_score = score_font.render(str(player2_score), True, (255, 50, 100))

        if ball.y >= 620 or ball.y <= 0:
            y_delta = y_delta * -1

        # player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player1.move_direction("player 1 up")
        if keys[pygame.K_s]:
            player1.move_direction("player 1 down")
        if keys[pygame.K_UP]:
            player2.move_direction("player 2 up")
        if keys[pygame.K_DOWN]:
            player2.move_direction("player 2 down")

        # if the ball collides with the player, make it bounce
        if ball.rect.colliderect(player1.rect) or ball.rect.colliderect(player2.rect):
            x_delta = x_delta * -1

        # point system
        screen.blit(display_player1_score, (300, 0))
        screen.blit(display_player2_score, (550, 0))

        # first to 7 points wins
        if player1_score == 7:
            game_over = True
            player1_win = True
        if player2_score == 7:
            game_over = True
            player2_win = True

    # final screen
    if game_over:
        screen.fill((0, 0, 0))
        if player1_win:
            p1_win_message = "Player 1 wins!"
            display_p1_win_message = win_font.render(p1_win_message, True, (50, 100, 255))
            screen.blit(display_p1_win_message, (325, 275))
        if player2_win:
            p2_win_message = "Player 2 wins!"
            display_p2_win_message = win_font.render(p2_win_message, True, (255, 50, 100))
            screen.blit(display_p2_win_message, (325, 275))
        # press space to play again
        play_again_message = "Press SPACE to play again!"
        display_play_again_message = my_font.render(play_again_message, True, (255, 255, 255))
        screen.blit(display_play_again_message, (300, 350))

    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
