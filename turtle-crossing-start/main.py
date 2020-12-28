import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars=[]

car = CarManager()
cars.append(car)
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move_up, "Up")

count=0

game_is_on = True
while game_is_on:
    count+=1

    time.sleep(car.carspeed)
    screen.update()

    if count % 6 == 0:
        car = CarManager()
        cars.append(car)



    for car in cars:
        car.move()
        if player.distance(car) < 20:
            print("Collison")
            game_is_on = False
            scoreboard.gameover()


    if player.ycor() > 250:
            player.restart()
            scoreboard.levelup()
            for car in cars:
                car.speedup()



screen.exitonclick()