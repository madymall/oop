import turtle

hw = turtle.Turtle()
sc = turtle.Screen()

sc.bgcolor('black')
hw.pencolor('#ff4040')

hw.speed(0)
hw.penup()
hw.goto(0, 100)
hw.pendown()

x = 0
y = 0

for i in range(210):
    hw.forward(x)
    hw.right(y)

    x += 2
    y += 1

turtle.done()