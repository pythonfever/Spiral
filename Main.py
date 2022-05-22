import turtle
screen = turtle.Screen()
screen. setup(500, 600, startx=0, starty=100)
t = turtle. Turtle()
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed (0)
while (True):
    for i in range(6):
        for colors in ["red", "blue", "magenta", "green","yellow", "white"]:
            turtle.color(colors)
            turtle.circle(100)
            turtle. left(10)
