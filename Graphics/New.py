import turtle

# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
star_turtle = turtle.Turtle()
star_turtle.shape("arrow")
star_turtle.speed(10)  # Set the drawing speed (1 is slowest, 0 is fastest)

# Function to draw a star
def draw_star(size):
    for _ in range(5):
        star_turtle.forward(size)
        star_turtle.right(120)

# Move the turtle to a starting position
star_turtle.penup()
star_turtle.goto(0,0)  # Adjust the starting position as needed
star_turtle.pendown()


# Set the star size
star_size = 200

# Draw the star
draw_star(star_size)
turtle.pencolor("white")

# Close the turtle graphics window on click
screen.exitonclick()
