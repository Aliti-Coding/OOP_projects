import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
score = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkey(turtle.up,"Up")
screen.onkey(turtle.Down, "Down")


score.text_level()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()
    


    # increase level if turtle cross finishline
    if turtle.ycor() > 280:
        turtle.finishline()
        score.increase_level()
        cars.increase_difficulty()

    #detect collison
    for car in cars.cars_lst:
        if car.distance(turtle) < 20:
            score.game_over()
            game_is_on = False


screen.exitonclick()