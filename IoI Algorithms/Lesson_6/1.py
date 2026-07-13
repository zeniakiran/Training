# ================================================
#  ACTIVITY - RAINBOW STAR PATTERN

# PART 1 - IMPORT MODULE AND CREATE DRAWING WINDOW
# Screen() creates the drawing area.
# bgcolor() changes the background color.
# title() displays a custom window title.
import turtle

canvas = turtle.Screen()
canvas.bgcolor("midnightblue")
canvas.title("Rainbow Star Pattern")

# PART 2 - CREATE THE DRAWING PEN
# Turtle() creates the pen that draws on the screen.
# speed("fastest") makes drawing almost instant.
# hideturtle() hides the turtle cursor.
artist = turtle.Turtle()
artist.speed("fastest")
artist.hideturtle()

# PART 3 - DRAW A COLORFUL SPIRAL
# The loop repeats several times.
# Each turn is slightly more than 90 degrees,
# creating a spiral effect instead of a square.
rainbow = ["white", "cyan", "magenta", "yellow", "lime", "orange", "red", "blue"]

for step in range(80):
    artist.color(rainbow[step % len(rainbow)])
    artist.width(2)
    artist.forward(step * 2)
    artist.right(91)

# PART 4 - MOVE TO THE CENTER AND DRAW A FILLED STAR
# penup() moves without drawing.
# goto() changes the turtle's position.
# setheading() points the turtle upward.
artist.penup()
artist.goto(0, -60)
artist.setheading(90)
artist.pendown()

artist.color("white", "gold")
artist.begin_fill()

for point in range(5):
    artist.forward(130)
    artist.right(144)

artist.end_fill()

# PART 5 - DRAW A RING OF FILLED SQUARES
# The outer loop rotates the turtle.
# The inner loop draws one filled square.
square_colors = ["skyblue", "springgreen", "hotpink", "gold", "plum"]

artist.penup()
artist.goto(0, 0)
artist.pendown()

for rotation in range(36):
    artist.color(
        square_colors[rotation % len(square_colors)],
        square_colors[(rotation + 1) % len(square_colors)]
    )

    artist.begin_fill()

    for side in range(4):
        artist.forward(55)
        artist.right(90)

    artist.end_fill()
    artist.right(10)

# KEEP THE WINDOW OPEN
turtle.done()