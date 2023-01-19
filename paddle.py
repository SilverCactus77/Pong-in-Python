import pygame

BLACK = (0, 0, 0)


class Paddle(pygame.sprite.Sprite):
    # The class represents a paddle which comes from the sprite class in pygame

    def __init__(self, color, width, height):
        # Call (Sprite) constructor
        super().__init__()

        # Designate the paddle colour and parameters
        # Set the background color to black and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draws the paddle (a rectangle)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # retrieves the rectangle object with its assigned parameters
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels
        # Makes sure the paddles don't go off the screen
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels
        # Makes sure the paddles don't go off the screen
        if self.rect.y > 400:
            self.rect.y = 400

