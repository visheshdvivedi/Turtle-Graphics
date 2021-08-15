import turtle
from turtle import*

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Happy Independace Day")
screen.setup(width = 1.0, height = 1.0)
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)

pen = turtle.Turtle()
speed(0)
FONT = ("Helvetica", 30, "italic")
# initially penup()
pen.penup()
pen.goto(-400, 250)
pen.pendown()

def drawOrangeRect(pen):
    pen.color("orange")
    pen.begin_fill()
    pen.forward(800)
    pen.right(90)
    pen.forward(167)
    pen.right(90)
    pen.forward(800)
    pen.end_fill()

def drawWhiteRect(pen):
    pen.color("white")
    pen.right(180)
    pen.begin_fill()
    pen.forward(800)
    pen.right(90)
    pen.forward(167)
    pen.right(90)
    pen.forward(800)
    pen.end_fill()

def drawGreenRect(pen):
    pen.color("green")
    pen.right(180)
    pen.begin_fill()
    pen.forward(800)
    pen.right(90)
    pen.forward(167)
    pen.right(90)
    pen.forward(800)
    pen.end_fill()

def drawBigBlueCircle(pen):
    pen.penup()
    pen.goto(0, 70)
    pen.pendown()
    pen.color("navy")
    pen.begin_fill()
    pen.circle(70)
    pen.end_fill()

def drawWhiteCircle(pen):
    pen.penup()
    pen.goto(0, 60)
    pen.pendown()
    pen.color("white")
    pen.begin_fill()
    pen.circle(60)
    pen.end_fill()

def drawMiniBlueCircles(pen):
    pen.penup()
    pen.goto(8, -57)
    pen.pendown()
    pen.color("navy")
    for i in range(24):
        pen.begin_fill()
        if i+1 in [15, 16, 17, 18, 19, 20, 21]:
            pen.circle(3.5)
        else:
            pen.circle(3)
        pen.end_fill()
        pen.penup()
        pen.forward(15)
        pen.right(15)
        pen.pendown()

def drawCenterBlueCircle(pen):
    pen.penup()
    pen.goto(0, 20)
    pen.pendown()
    pen.begin_fill()
    pen.circle(20)
    pen.end_fill()

def drawSpokes(pen):
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.pensize(2)
    for i in range(24):
        pen.forward(60)
        pen.backward(60)
        pen.left(15)

def writeText(score):
    global turtle
    global FONT
    score.hideturtle()
    score.speed('fastest')
    score.penup()
    score.sety(275)
    score.setx(-200)
    score.color("orange")
    score.write("Happy", move=True, font=FONT)
    score.color("white")
    score.write(" Independance", move=True, font=FONT)
    score.color("green")
    score.write(" Day", move=True, font=FONT)

drawOrangeRect(pen)
drawWhiteRect(pen)
drawGreenRect(pen)
drawBigBlueCircle(pen)
drawWhiteCircle(pen)
drawMiniBlueCircles(pen)
drawCenterBlueCircle(pen)
drawSpokes(pen)
writeText(pen)
turtle.done()
