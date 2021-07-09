import turtle

window = turtle.Screen()
window.bgcolor("black")
window.title("Instagram Logo")

pen = turtle.Turtle()
pen.shape('turtle')

def drawQuaterCircle(pen):
    for _ in range(90):
        pen.right(1)
        pen.forward(1)

def createBox(pen):
    pen.color('red')
    pen.fillcolor('red')
    pen.penup()
    pen.goto(0, 100)
    pen.pendown()
    pen.begin_fill()
    for _ in range(4):
        pen.forward(100)
        drawQuaterCircle(pen)
        pen.forward(100)
    pen.end_fill()

def createWhiteBox(pen, size, color):
    pen.color(color)
    pen.fillcolor(color)
    pen.penup()
    pen.goto(0, size)
    pen.pendown()
    pen.begin_fill()
    for _ in range(4):
        pen.forward(size)
        drawQuaterCircle(pen)
        pen.forward(size)
    pen.end_fill()

def createWhiteCircle(pen, size, color, pos_x, pos_y):
    pen.color(color)
    pen.fillcolor(color)
    pen.penup()
    pen.goto(pos_x, pos_y)
    pen.pendown()
    pen.begin_fill()
    pen.circle(size)
    pen.end_fill()

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
    turtle.write("Instagram Logo", font=("Helvetica", 30, "italic"), align="center")
    turtle.penup()
    turtle.goto(0, 150)
    turtle.pendown()
    turtle.write("By:- All About Python", font=("Helvetica", 20, "italic"), align="center")
    turtle.color('black')

if __name__ == '__main__':
    createBox(pen)
    createWhiteBox(pen, 60, 'white')
    createWhiteBox(pen, 40, 'red')
    createWhiteCircle(pen, 60, 'white', 0, -120)
    createWhiteCircle(pen, 40, 'red', 0, -100)
    createWhiteCircle(pen, 10, 'white', 50, 0)
    positionPen(pen)
    writeText()
    turtle.done()
