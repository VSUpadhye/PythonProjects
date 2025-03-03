from turtle import Turtle, Screen
import random

colors = ["red", "green", "blue", "dark orange", "maroon", "purple", "chocolate"]
turtles = ["t1", "t2", "t3", "t4", "t5", "t6", "t7"]

screen = Screen()
screen.setup(width= 500, height= 500)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

y = -150
for _ in range(7):
    turtles[_] = Turtle(shape="turtle")
    turtles[_].color(colors[_])
    turtles[_].penup()
    turtles[_].goto(x= -230, y= y)
    y += 50

race_on = False
if user_bet:
    race_on = True

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_dist = random.randint(0, 10)
        turtle.forward(random_dist)
screen.exitonclick()