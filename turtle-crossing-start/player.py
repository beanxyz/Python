from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)


    def move_up(self):
        print(self.xcor(), self.ycor())

        self.forward(MOVE_DISTANCE)
        print(self.xcor(),self.ycor())

    def restart(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)
