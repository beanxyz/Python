from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("gold")
        self.penup()
        self.hideturtle()
        self.lscore=0
        self.rscore=0
        self.update_score()

    def update_score(self):
        self.goto(-80, 250)
        self.write(self.lscore, align="center", font=("Courier", 40, "normal"))
        self.goto(80, 250)
        self.write(self.rscore, align="center", font=("Courier", 40, "normal"))
        self.goto(0,0)

    def l_score(self):
        self.lscore+=1
        self.clear()
        self.update_score()


    def r_score(self):
        self.rscore+=1
        self.clear()
        self.update_score()