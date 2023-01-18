import pygame
from random import randint

BLACK = (0, 0, 0)


class Ball(pygame.sprite.Sprite):
    # This class makes a sprite called ball which comes from the pygame library

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # set the colour of the ball and its width and height
        # Sets the background color as black and sets it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draws the ball in the shape of a rectangle and defines its dimensions
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(4, 8), randint(-8, 8)]

        # Gets the rectangle with dimensions that were defined before
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)