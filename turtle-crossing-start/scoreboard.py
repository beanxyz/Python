from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("Black")
        self.level = 1
        self.update()

    def update(self):
        self.goto(-200,260)
        self.clear()
        self.write(f"Level : {self.level} ", align='Center', font = FONT)


    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER",align='Center',font=FONT)

    def levelup(self):
        self.level += 1
        self.update()

