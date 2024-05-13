import pygame


class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("player.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def move_direction(self, direction):
        if direction == "player 1 up" and not self.y <= 0:
            self.y = self.y - 0.6
        if direction == "player 1 down" and not self.y >= 560:
            self.y = self.y + 0.6
        if direction == "player 2 up" and not self.y <= 0:
            self.y = self.y - 0.6
        if direction == "player 2 down" and not self.y >= 560:
            self.y = self.y + 0.6
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
