import turtle
n = int(input())
def polygon(n):
    ben = turtle.Turtle()
    ben.speed(0)
    for x in range(n):
        ben.forward(7)
        ben.left((360/n))
polygon(n)
