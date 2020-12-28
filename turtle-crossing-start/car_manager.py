from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_len=2,stretch_wid=1)
        self.setheading(180)
        self.penup()
        self.goto(300,random.randint(-250,250))
        self.carspeed=0.1

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)


    def speedup(self):
        self.carspeed *= 0.9