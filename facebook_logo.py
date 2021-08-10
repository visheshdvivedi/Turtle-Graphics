import turtle

window = turtle.Screen()
window.bgcolor("black")
window.title("Facebook Logo")

pen = turtle.Turtle()
pen.shape('turtle')

def drawQuaterCircle(pen):
    for _ in range(45):
        pen.right(2)
        pen.forward(0.5)

def createBox(pen):
    pen.color('blue')
    pen.fillcolor('blue')
    pen.penup()
    pen.goto(0, 100)
    pen.pendown()
    pen.begin_fill()
    for _ in range(4):
        pen.forward(100)
        drawQuaterCircle(pen)
        pen.forward(100)
    pen.end_fill()

def drawFQuarterCircle(pen):
    for _ in range(90):
        pen.right(1)
        pen.forward(0.7)

def drawSecondFQuarterCircle(pen):
    for _ in range(90):
        pen.left(1)
        pen.forward(0.35)

def positionPen(pen):
    pen.penup()
    pen.goto(0, 250)
    pen.right(90)
    pen.pendown()

def writeText():
    global turtle
    turtle.color('white')
    turtle.penup()
    turtle.goto(0, 190)
    turtle.pendown()
    turtle.write("Facebook Logo", font=("Helvetica", 30, "italic"), align="center")
    turtle.penup()
    turtle.goto(0, 150)
    turtle.pendown()
    turtle.write("By:- All About Python", font=("Helvetica", 20, "italic"), align="center")
    turtle.color('black')


createBox(pen)
pen.color('white')
pen.penup()
pen.goto(0, -130)
pen.pendown()
pen.fillcolor('white')
pen.begin_fill()
pen.left(90)
pen.forward(80)
pen.left(90)
pen.forward(30)
pen.right(90)
pen.forward(30)
pen.right(90)
pen.forward(30)
pen.left(90)
pen.forward(30)
drawFQuarterCircle(pen)
pen.forward(15)
pen.right(90)
pen.forward(30)
pen.right(90)
pen.forward(7.5)
drawSecondFQuarterCircle(pen)
pen.forward(20)
pen.left(90)
pen.forward(30)
pen.right(95)
pen.forward(32)
pen.right(85)
pen.forward(28)
pen.left(90)
pen.forward(80)
pen.right(90)
pen.forward(30)
pen.end_fill()
positionPen(pen)
writeText()
turtle.done()