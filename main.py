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




