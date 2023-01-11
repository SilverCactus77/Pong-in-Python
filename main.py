import turtle as t

playerAscore = 0
playerBscore = 0

# create a window and declare a variable called window and call the screen()
window = t.Screen()
window.title("Pong")
window.bgcolor("blue")
window.setup(width=800, height=600)
window.tracer(0)

#Creating the left paddle
leftpaddle=t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5,stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350,0)