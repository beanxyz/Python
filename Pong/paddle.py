from turtle import Turtle


class Paddle(Turtle):

    def __init__(self,x,y):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(x, y)

           # self.segments.append(seg)


    def up(self):
        #self.pad.setheading(90)
        new_y=self.ycor()+20
        # print("UP")
        self.goto(self.xcor(),new_y)


    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



    # def moveup(self):
    #     for seg in range(len(self.segments)-1,0,-1):
    #         new_x = self.segments[seg-1].xcor()
    #         new_y = self.segments[seg-1].ycor()
    #         self.segments[seg].goto(new_x,new_y)
    #     self.head.forward(20)
    #
    # def movedown(self):
    #     for seg in range(0,len(self.segments)):
    #         new_x = self.segments[seg+1].xcor()
    #         new_y = self.segments[seg+1].ycor()
    #         print(seg,new_x,new_y)
    #         self.segments[seg].goto(new_x, new_y)
    #     self.tail.forward(20)