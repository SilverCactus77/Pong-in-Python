import pygame
from random import randint

BLACK = (0, 0, 0)


class Ball(pygame.sprite.Sprite):
    # This class represents a ball and uses the sprite class from pygame

    def __init__(self, color, width, height):
        # Call the (Sprite) constructor
        super().__init__()

        # Defines the colour of the ball and its parameters
        # Set the background color to black and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the ball (also a rectangle)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(4, 8), randint(-8, 8)]

        # retrieves the proper rectangle with its parameters
        self.rect = self.image.get_rect()

    def update(self):
        # Sets velocity of the ball
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        # Sets the velocity of the ball
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)