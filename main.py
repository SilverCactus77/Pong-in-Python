# Import the pygame library and initialise the game engine
# Also import Paddle class and Ball class
import pygame
from paddle import Paddle
from ball import Ball

pygame.init()

# Defines colors for game
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Opens a new window
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

# This list contains all sprites in the code
all_sprites_list = pygame.sprite.Group()

# Adds the paddles to the list of sprites
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

# This loop carries on until user exits game
carryOn = True

# The clock is used to control how fast the screen updates
clock = pygame.time.Clock()

# Initialises player scores
scoreA = 0
scoreB = 0

# Main Program Loop
while carryOn:
    # Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # signifies to exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                carryOn = False

    # Designates controls to each player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)

    # This is the game logic
    all_sprites_list.update()

    # Checks if the ball is bouncing against any of the 4 walls
    if ball.rect.x >= 690:
        scoreA += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        scoreB += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

        # Detects collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()


    # Clears the screen to black
    screen.fill(BLACK)
    # Draws the line in middle of screen
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

    # Draws all the sprites at once
    all_sprites_list.draw(screen)

    # Displays scores
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250, 10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420, 10))

    # Updates the screen with what was drawn
    pygame.display.flip()

    # Limits game to 60 frames per second
    clock.tick(60)

    # exits main code loop
    pygame.quit()










