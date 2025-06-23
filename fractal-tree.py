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
        left(angle_r)

        backward(length)

tracer(0)
penup()
goto(0, -200)
pendown()
left(90)
grow(100, 0.8, 30)

#tracer(0)
exitonclick()