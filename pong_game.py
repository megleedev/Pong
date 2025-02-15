import turtle

# Draw the screen
screen = turtle.Screen()
screen.setup (width = 800, height = 600)
screen.title ("Pong")
screen.bgcolor ("black")
screen.tracer (0)

# Create setup for center line
center_line = turtle.Turtle ()
center_line.color ("white")
center_line.speed (0)
center_line.hideturtle ()

# Move to center line starting position
center_line.penup ()
center_line.goto (0, 300)
center_line.setheading (270)

# Draw the center line
for d in range (40):
    center_line.pendown ()
    center_line.forward (10)
    center_line.penup ()
    center_line.forward (10)

# Draw the left paddle and set initial position
left_paddle = turtle.Turtle ()
left_paddle.shape ("square")
left_paddle.shapesize (stretch_wid = 4, stretch_len = 1)
left_paddle.color ("white")
left_paddle.speed (0)
left_paddle.penup ()
left_paddle.goto (-350, 0)

# Draw the right paddle and set initial position
right_paddle = turtle.Turtle ()
right_paddle.shape ("square")
right_paddle.shapesize (stretch_wid = 4, stretch_len = 1)
right_paddle.color ("white")
right_paddle.speed (0)
right_paddle.penup ()
right_paddle.goto (350, 0)

# Draw the ball and set initial position
ball = turtle.Turtle ()
ball.shape ("square")
ball.shapesize (stretch_wid = 1, stretch_len = 1)
ball.color ("white")
ball.speed (40)
ball.penup ()
ball.goto (0, 0)
ball.dx = 5
ball.dy = -5

screen.update ()

# Keeps the window open after the program completes
turtle.done ()