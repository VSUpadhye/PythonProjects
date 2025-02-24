#import colorgram
#
# colors = colorgram.extract('image.jpg', 25)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

from turtle import Turtle, Screen
import turtle
import random

turtle.colormode(255)

rgb_colors = [(132, 166, 205), (221, 148, 106),(32, 42, 61), (199, 135, 148), (166, 58, 48),(141, 184, 162),
              (39, 105, 157), (237, 212, 90),(150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157),
              (51, 111, 90), (35, 61, 55), (156, 33, 31),(17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221),
              (57, 51, 48), (184, 103, 113)]

timmy = Turtle()
timmy.shape('classic')
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)


for x in range(1, 101):
    timmy.dot(15, random.choice(rgb_colors))
    timmy.forward(50)

    if x % 10 == 0:
        timmy.left(90)
        timmy.forward(50)
        timmy.left(90)
        timmy.forward(500)
        timmy.setheading(0)

screen = Screen()
screen.exitonclick()