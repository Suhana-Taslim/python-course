import turtle

turtle.Screen().bgcolor("Blue")

sc=turtle.Screen()
sc.setup(1000,1000)

turtle.title("Printing Polygons")

board=turtle.Turtle()
draw=turtle.Turtle()

for i in range(3):
    board.forward(100)
    board.left(120)
    i = i+1
    
board.penup()
board.forward(150)
board.pendown()

for n in range(4):   
    draw.forward(200)
    draw.left(90)
    n = n+1