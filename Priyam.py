import turtle as t

screen = t.Screen()
screen.bgcolor("darkgrey")

t.pensize(5)
t.speed(2)
t.color("red")
t.penup()

start_x = -screen.window_width() // 2 + 50
start_y = 0 
t.goto(start_x, start_y)

def reset_position(dx=0, dy=0):
    t.penup()
    t.setheading(0)  
    t.forward(dx)
    t.right(90)
    t.forward(dy)
    t.left(90)

def write_P():
    t.pendown()
    t.left(90)
    t.forward(60)

    t.right(90)

    t.circle(-15,180)
    t.pendown()
    reset_position(dx=20)

def write_R():
    t.goto(start_x+25,start_y)
    t.pendown()
    t.left(90)
    t.forward(60)

    t.right(90)

    t.circle(-15,180)

    t.left(115)
    t.forward(33)

    reset_position(dx=10)

def write_I():
    t.goto(start_x+60,start_y)
    t.pendown()
    t.left(90)
    t.forward(60)

    t.left(90)
    t.forward(10)
    t.backward(20)
    t.penup()

    t.goto(start_x+60,start_y)
    t.pendown()
    t.left(180)
    t.forward(10)
    t.backward(20)

    reset_position(dx=15)

def write_Y():
    t.goto(start_x+100,start_y)
    t.pendown()
    t.left(90)
    t.forward(35)
    t.right(35)
    t.forward(30)
    t.penup()

    t.goto(start_x+100,start_y)
    t.pendown()
    t.left(35)
    t.forward(35)
    t.left(35)
    t.forward(30)

    reset_position(dx=10)
    
def write_A():
    t.goto(start_x+120,start_y)
    t.pendown()
    t.left(70)
    t.forward(60)
    
    t.right(140)
    t.forward(60)
    
    t.penup()
    t.goto(start_x+120,start_y)
    t.left(140)
    t.forward(30)
    t.right(70)
    t.pendown()
    t.forward(20)
    reset_position(dx=10)

def write_M():
    t.goto(start_x+170,start_y)
    t.pendown()
    t.left(90)
    t.forward(60)

    t.right(135)
    t.forward(25)

    t.left(90)
    t.forward(25)

    t.right(135)
    t.forward(60)

    
write_P()
write_R()
write_I()
write_Y()
write_A()
write_M()

t.hideturtle()
screen.mainloop()

screen.exitonclick