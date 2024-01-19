import turtle

def draw_star(size):
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)

def main():
    turtle.speed(5)  # Set the drawing speed (1 is the slowest, 10 is the fastest)
    turtle.pensize(1)  # Set the pen size
    turtle.pencolor("red")  # Set the pen color

    star_size = 150
    draw_star(star_size)

    turtle.done()

if __name__ == "__main__":
    main()
