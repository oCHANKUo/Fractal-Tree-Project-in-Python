from turtle import *
#from theme import set_theme
import random

#function to grow tree, recursive
def grow(length, decrease, angle, noise=0):

    if length > 10:
        forward(length)


penup()
goto(0, -400)
pendown()
left(90)
grow(150, 1, 0)

tracer(0)
exitonclick()