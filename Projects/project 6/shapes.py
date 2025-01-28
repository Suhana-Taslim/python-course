import turtle

def triangle():
    for _ in range(3):
        turtle.forward(100)
        turtle.left(120)

def rectangle():
    for _ in range(2):
        turtle.forward(150)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)

def hexagon():
    for _ in range(6):
        turtle.forward(80)
        turtle.left(60)


screen = turtle.Screen()
screen.title("Drawing Shapes with Turtle")


turtle.penup()
turtle.goto(-200, 100)
turtle.pendown()
turtle.color("blue")
triangle()


turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.color("green")
rectangle()


turtle.penup()
turtle.goto(200, 100)
turtle.pendown()
turtle.color("purple")
hexagon()