from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width= 800, height= 600)
screen.title("PONG")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle(x = 370, y = 0)
l_paddle = Paddle(x = -375, y = 0)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    # Detect collision with any paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # Ball misses the right paddle
    if ball.xcor() > 450:
        ball.reset_pos()
        score.l_point()

    # Ball misses the left paddle
    if ball.xcor() < -450:
        ball.reset_pos()
        score.r_point()

screen.exitonclick()