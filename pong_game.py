import turtle
import time

# Draw the screen
screen = turtle.Screen()
screen.setup (width = 800, height = 600)
screen.title ("Pong")
screen.bgcolor ("black")
screen.tracer (0) # Disables incremental screen updates

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

# Displays the scores on the screen
score = turtle.Turtle ()
score.color ("white")
score.speed (0)
score.penup ()
score.hideturtle ()
score.goto (0, 200)
score.write ("00 00", align = "center", font = ("Courier", 50, "normal"))

# Updates the screen after drawing board objects
screen.update ()

# Functions to move pong paddles
def left_paddle_up ():
    y = left_paddle.ycor ()
    if y < 250:
        y += 20
        left_paddle.sety (y)

def left_paddle_down ():
    y = left_paddle.ycor ()
    if y > -240:
        y -= 20
        left_paddle.sety (y)

def right_paddle_up ():
    y = right_paddle.ycor ()
    if y < 250:
        y += 20
        right_paddle.sety (y)

def right_paddle_down ():
    y = right_paddle.ycor ()
    if y > -240:
        y -= 20
        right_paddle.sety (y)

# Initialize the starting scores
left_score = 0
right_score = 0

# Keyboard bindings
screen.listen ()
screen.onkeypress (left_paddle_up, "w")
screen.onkeypress (left_paddle_down, "s")
screen.onkeypress (right_paddle_up, "Up")
screen.onkeypress (right_paddle_down, "Down")



# Main game loop
while True:
    screen.update ()
    time.sleep (0.01)

    # Moves the ball
    ball.setx (ball.xcor () + ball.dx)
    ball.sety (ball.ycor () + ball.dy)

    # Checks for collision with the game board boundaries
    if ball.ycor () > 280:
        ball.sety (280)
        ball.dy *= -1

    if ball.ycor () < -280:
        ball.sety (-280)
        ball.dy *= -1

    if ball.xcor () > 500:
        ball.goto (0, 0)
        ball.dy *= -1
        left_score += 1
        score.clear ()
        score.write ("{} {}".format (left_score, right_score), align = "center", font = ("Courier", 50, "normal"))

    if ball.xcor () < -500:
        ball.goto (0, 0)
        ball.dy *= -1
        right_score += 1
        score.clear ()
        score.write ("{} {}".format (left_score, right_score), align = "center", font = ("Courier", 50, "normal"))

    # Checks for collision with the paddles
    if (ball.xcor () > 360 and ball.xcor () < 370) and \
        (ball.ycor () < right_paddle.ycor () + 50 and ball.ycor () > right_paddle.ycor () - 50):
        ball.setx (360)
        ball.dx *= -1

    if (ball.xcor () < -360 and ball.xcor () > -370) and \
        (ball.ycor () < left_paddle.ycor () + 50 and ball.ycor () > left_paddle.ycor () - 50):
        ball.setx (-360)
        ball.dx *= -1