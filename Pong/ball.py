from turtle import  Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x=10
        self.y=10
        self.move_speed=0.1

    def move(self):
        # self.setheading(60)
        # self.forward(10)
        self.goto(self.xcor()+self.x,self.ycor()+self.y)
        # print(self.xcor(),self.ycor())

    def bounce_x(self):


        self.y*=-1


    def bounce_y(self):
        self.x *= -1

    def reset_posiiton(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed=0.1
