from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("The Snack Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_on = True
while is_on:
    screen.update()
    time.sleep(.1)

    snake.move()

    # Detecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.append_segment()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_score()
        snake.reset_snake()

    # Detect collision with tail
    for segment in snake.segments[1 : ]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset_snake()

screen.exitonclick()