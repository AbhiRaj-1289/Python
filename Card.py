# import turtle

# screen = turtle.Screen()
# screen.bgcolor("white")
# screen.title("Greeting Card")

# card = turtle.Turtle()
# card.speed(3)

# def draw_heart():
#     card.color("red")
#     card.pensize(5)
#     card.begin_fill()
#     card.left(140)
#     card.forward(180)
#     card.circle(-90, 200)
#     card.left(120)
#     card.circle(-90, 200)
#     card.forward(180)
#     card.end_fill()

# def write_message(message):
#     card.penup()
#     card.goto(0, -200)
#     card.color("red")
#     card.write(message, align="center", font=("Arial", 36, "bold"))
#     card.hideturtle()

# draw_heart()

# write_message("Give Your All Sadness To Me\nAlways Be Happy")

# turtle.done()

import turtle
import time

screen = turtle.Screen()
screen.bgcolor("lightpink")
screen.title("Special Greeting Card")

border = turtle.Turtle()
border.speed(10)
border.color("purple")

def draw_border():
    border.penup()
    border.goto(-200, -200)
    border.pendown()
    border.pensize(5)
    for _ in range(4):
        border.forward(400)
        border.left(90)
    border.hideturtle()

heart = turtle.Turtle()
heart.color("red")
heart.speed(10)

def draw_heart():
    heart.penup()
    heart.goto(0, 0)
    heart.pendown()
    heart.begin_fill()
    heart.left(140)
    heart.forward(180)
    heart.circle(-90, 200)
    heart.left(120)
    heart.circle(-90, 200)
    heart.forward(180)
    heart.end_fill()

def animate_heart():
    for _ in range(3):
        heart.clear()
        draw_heart()
        heart.shapesize(1.2)
        time.sleep(0.5)
        heart.clear()
        draw_heart()
        heart.shapesize(1)
        time.sleep(0.5)
    heart.hideturtle()

message_turtle = turtle.Turtle()
message_turtle.speed(10)

def write_message():
    message_turtle.penup()
    message_turtle.goto(0, -100)
    message_turtle.color("red")
    message_turtle.write("So Lucky I Am\nTo Have You Back", align="center", font=("Courier", 24, "bold"))
    message_turtle.hideturtle()

stars = turtle.Turtle()
stars.color("yellow")
stars.speed(10)

def draw_star(x, y):
    stars.penup()
    stars.goto(x, y)
    stars.pendown()
    stars.begin_fill()
    for _ in range(5):
        stars.forward(40)
        stars.right(144)
    stars.end_fill()

def add_decorations():
    positions = [(-150, 150), (150, 150), (-150, -150), (150, -150)]
    for pos in positions:
        draw_star(pos[0], pos[1])
    stars.hideturtle()

draw_border()
animate_heart()
write_message()
add_decorations()

turtle.done()
