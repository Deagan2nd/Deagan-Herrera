#-------------------------------------------------------------------------------
# Name:        3.8 Prob. 11
# Purpose:
#
# Author:      drherrera
#
# Created:     09/09/2025
# Copyright:   (c) drherrera 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
alex = turtle.Turtle()
alex.shape("turtle")
alex.hideturtle()
for i in range (8):
    alex.forward(100)
    alex.right(144)
wn.mainloop()