import turtle as t

playerAscore = 0
playerBscore = 0

# create a window and declare a variable called window and call the screen()
window = t.Screen()
window.title("Pong")
window.bgcolor("blue")
window.setup(width=800, height=600)
window.tracer(0)

# Creating the left paddle
lp = t.Turtle()
lp.speed(0)
lp.shape("square")
lp.color("white")
lp.shapesize(stretch_wid=5, stretch_len=1)
lp.penup()
lp.goto(-350, 0)

# Creating the right paddle
rp = t.Turtle()
rp.speed(0)
rp.shape("square")
rp.color("White")
rp.shapesize(stretch_wid=5, stretch_len=1)
rp.penup()
rp.goto(350, 0)

