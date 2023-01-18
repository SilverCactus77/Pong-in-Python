# Import the pygame library and initialise the game engine
import pygame
from paddle import Paddle
from ball import Ball

pygame.init()

# Defines some colors for the game
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

# This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

# Add the paddles to the list of sprites
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)

# Add the paddles and the ball to the list of objects
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# Main Program Loop
while carryOn:
    # Main event loop
    for event in pygame.event.get():  # user does something
        if event.type == pygame.QUIT:  # If user clicks quit
            carryOn = False  # exits the loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # pressing the x key will end the game
                carryOn = False

            # Moving the paddles when the user uses the arrow keys (player A) or "W/S" keys (player B)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                    paddleA.moveUp(5)
            if keys[pygame.K_s]:
                    paddleA.moveDown(5)
            if keys[pygame.K_UP]:
                    paddleB.moveUp(5)
            if keys[pygame.K_DOWN]:
                    paddleB.moveDown(5)

            # Check if the ball is bouncing against any of the 4 walls:
            if ball.rect.x >= 690:
                        ball.velocity[0] = -ball.velocity[0]
            if ball.rect.x <= 0:
                        ball.velocity[0] = -ball.velocity[0]
            if ball.rect.y > 490:
                        ball.velocity[1] = -ball.velocity[1]
            if ball.rect.y < 0:
                        ball.velocity[1] = -ball.velocity[1]

            # Detect collisions between the ball and the paddles
            if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
                ball.bounce()

all_sprites_list.update()

# Drawing code should go here
# clears the screen to black.
screen.fill(BLACK)
# Draws the net
pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

# draws all the sprites at the same time
all_sprites_list.draw(screen)

# updates the screen with new sprites
pygame.display.flip()

# Limits game to 60 frames per second
clock.tick(60)

# exits the main program loop
pygame.quit()










