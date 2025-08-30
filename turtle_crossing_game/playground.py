from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_car()
    carmanager.move_all_cars()

    # detect collision
    for car in carmanager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()


    # if reached finish line
    if player.is_at_finsh_line():
        player.goto_start()
        carmanager.level_up()
        scoreboard.increase_level()


screen.exitonclick()