from turtle import Turtle

MOVE_DISTANCE = 15
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(0, -280)

    def up(self):
        self.forward(MOVE_DISTANCE)