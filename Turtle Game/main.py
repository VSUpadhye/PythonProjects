from turtle import Screen
from car_manager import CarManager
from player import Player
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width= 600, height= 600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(player.up, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_on = False

    if player.ycor() > 280:
        player.goto(0, -280)
        car_manager.level_up()
        scoreboard.increment_level()

screen.exitonclick()