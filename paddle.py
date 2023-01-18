import pygame

BLACK = (0, 0, 0)


class Paddle(pygame.sprite.Sprite):
    # This is a class which retrieves a sprite from the pygame library

    def __init__(self, color, width, height):
        # Calls the parent class (Sprite) constructor
        super().__init__()

        # defines the paddle colour,its width, and its height
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draws the paddle in the shape of a rectangle
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Retrieves the parameters of the rectangle
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels
        # Makes sure it doesn't go too far off the screen
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels
        # Makes sure it doesn't go too far off the screen
        if self.rect.y > 400:
            self.rect.y = 400

