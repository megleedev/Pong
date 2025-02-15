import turtle

# Function to display the start screen before the game starts
def show_start_screen (start_game_callback):
    start_screen = turtle.Screen ()
    start_screen.bgcolor ("black")
    start_screen.setup (width = 800, height = 600)
    start_screen.title ("Pong")
    
    start_text = turtle.Turtle ()
    start_text.color ("white")
    start_text.hideturtle ()

    # Displays the start screen text
    start_text.penup ()
    start_text.goto (0, 100)
    start_text.write ("PONG", align = "center", font = ("Courier", 50, "normal"))

    start_text.goto (0, 30)
    start_text.write ("Press SPACE to Start", align = "center", font = ("Courier", 20, "normal"))

    # Function to start the game when the player presses the SPACE key
    def on_space_pressed ():
        start_text.clear ()
        start_screen.clear ()
        start_game_callback ()

    # Wait for the player to press the SPACE key to start the game
    start_screen.listen ()
    start_screen.onkeypress (on_space_pressed, "space")
    turtle.mainloop ()