import turtle as t

# Player score at the beginning of the game
playerAscore = 0
playerBscore = 0

# Create a window for the game and import screen form turtle
window = t.Screen()
window.title("Pong")
window.bgcolor("blue")
window.setup(width=800, height=600)
window.tracer(0)

# Creates the left paddle
lp = t.Turtle()
lp.speed(0)
lp.shape("square")
lp.color("white")
lp.shapesize(stretch_wid=5, stretch_len=1)
lp.penup()
lp.goto(-350, 0)

# Creates the right paddle
rp = t.Turtle()
rp.speed(0)
rp.shape("square")
rp.color("White")
rp.shapesize(stretch_wid=5, stretch_len=1)
rp.penup()
rp.goto(350, 0)

# Creates the ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(5, 5)
ballxdirection=0.2
ballydirection=0.2

# This code makes a display for player scores
display = t.Turtle()
display.speed(0)
display.color("blue")
display.penup()
display.hideturtle()
display.goto(0, 260)
display.write("score", align="center", font=('Arial', 24, 'normal'))

# code for moving left paddle
def lpup():
    y = lp.ycor()
    y = y + 90
    lp.sety(y)

def lpdown():
    y = lp.ycor()
    y = y + 90
    lp.sety(y)

# code for moving right paddle
def rpup():
    y = rp.ycor()
    y = y + 90
    rp.set(y)

def rpdown():
    y = rp.ycor()
    y = y + 90
    rp.set(y)

# Assign controls to play
window.listen()
window.onkeypress(lpup, 'w')
window.onkeypress(lpdown, 's')
window.onkeypress(rpup, 'Up')
window.onkeypress(rpdown, 'Down')

while True:
    window.update()

    # moving the ball
    ball.setx(ball.xcor() + ballxdirection)
    ball.sety(ball.ycor() + ballxdirection)

# setting up a border
    if ball.ycor() > 290:
        ball.sety(290)
        ballydirection = ballydirection*-1
    if ball.ycor() < -290:
        ball.sety(-290)
        ballydirection = ballydirection*-1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball_dx = ball_dx * -1
        player_a_score = player_a_score + 1
        display.clear()
        display.write("Player A: {}  Player B: {} ".format(player_a_score, player_b_score),
                  align="center", font=('Monaco', 24, "normal"))
        os.system("afplay wallhit.wav&")

    if(ball.xcor()) < -390:
        # Left width paddle Border
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        player_b_score = player_b_score + 1
        display.clear()
        display.write("Player A: {}  Player B: {} ".format(player_a_score, player_b_score), align="center", font=('Monaco', 24, "normal"))
        os.system("afplay wallhit.wav&")

# Handling the collisions with paddles.

    if (ball.xcor() > 340) and (ball.xcor() < 350) and (
            ball.ycor() < rp.ycor() + 40 and ball.ycor() > rp.ycor() - 40):
        ball.setx(340)
        ball_dx = ball_dx * -1
        os.system("afplay paddle.wav&")

    if (ball.xcor() < -340) and (ball.xcor() > -350) and (
            ball.ycor() < lp.ycor() + 40 and ball.ycor() > lp.ycor() - 40):
        ball.setx(-340)
        ball_dx = ball_dx * -1
        os.system("afplay paddle.wav&")





