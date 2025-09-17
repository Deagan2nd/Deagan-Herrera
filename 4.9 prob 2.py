#-------------------------------------------------------------------------------
# Name: 4.9 prob 2
# Purpose:
#
# Author:      drherrera
#
# Created:     17/09/2025
# Copyright:   (c) drherrera 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle

def draw_square(t, sz):
    """Make turtle t draw a multi-color square of sz."""
    for i in range(5):
        t.forward(sz)
        t.left(90)
wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pensize(3)
tess.speed(0)
size = 150
for color in ["red", "purple", "hotpink", "blue"]:
    tess.color(color)
for i in range(5):

    tess.pendown()
    draw_square(tess, size)
    tess.penup()
    tess.forward(10)
    tess.left(90)
    tess.forward(10)
    tess.right(90)
    size = size - 20

wn.mainloop()
