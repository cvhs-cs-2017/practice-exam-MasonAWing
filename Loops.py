"""Use a loop to make a turtle draw a shape that is has at least 100 sides and
that shows symmetry.  The entire shape must fit inside the screen"""
import turtle
ben = turtle.Turtle()
for x in range(100):
    ben.forward(10)
    ben.right(360/100)
input()
