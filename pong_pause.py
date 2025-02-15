import turtle

# Global variable to keep track of whether the game is paused
game_paused = False
pause_text = None

# Function to end the game when the player presses the ESC key
def on_esc_pressed ():
    turtle.bye ()

def on_p_pressed ():
    global game_paused, pause_text
    game_paused = not game_paused

    if game_paused:
        pause_text = turtle.Turtle ()
        pause_text.color ("white")
        pause_text.hideturtle ()

        # Displays the start screen text
        pause_text.penup ()
        pause_text.goto (0, 100)
        pause_text.write ("PAUSE", align = "center", font = ("Courier", 50, "normal"))

        pause_text.goto (0, 30)
        pause_text.write ("Press P to Resume", align = "center", font = ("Courier", 20, "normal"))

        pause_text.goto (0, -10)
        pause_text.write ("Press Escape to Close", align = "center", font = ("Courier", 20, "normal"))

    else:
        pause_text.clear ()
        pause_text.hideturtle ()

# Function for the pause controls once on the pause screen
def pause_controls (screen):
    screen.listen ()
    screen.onkey (on_esc_pressed, "Escape")
    screen.onkey (on_p_pressed, "p")