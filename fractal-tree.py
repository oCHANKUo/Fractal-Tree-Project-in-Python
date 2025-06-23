from turtle import *
#from theme import set_theme
import random

#function to grow tree, recursive
def grow(length, decrease, angle, noise=0):

    if length > 10:
        forward(length)
        new_length = length * decrease
        angle_l = angle
        angle_r = angle

        left(angle_l)
        grow(new_length, decrease, angle, noise)
        right(angle_l)

        right(angle_r)
        grow(new_length, decrease, angle, noise)
        right(angle_r)


penup()
goto(0, -400)
pendown()
left(90)
grow(150, 0.8, 0)

tracer(0)
exitonclick()