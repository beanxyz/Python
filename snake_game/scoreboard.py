
from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial",20,"normal")



#显示分数和Game over等标记

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score=0
        self.highestscore = self.load_highestscore()
        self.updatescore()


    def load_highestscore(self):
        with open("highest.txt","r+") as f:
            highestscore= f.read()
            print(highestscore)
            if highestscore == '':
                highestscore = 0
                f.write('0')
            print(highestscore)


        return highestscore

    def updatescore(self):
        self.goto(0, 270)
        self.write(f"SCORE = {self.score}, HIGHTEST SCORE= {self.highestscore}",True, align=ALIGNMENT,font=FONT)
        self.goto(0,250)
#        self.write("-"*300,True, align=ALIGNMENT,font=FONT)

    def addscore(self):
        self.score+=1

        print(self.highestscore)
        if self.score > int(float(self.highestscore)):
            self.highestscore = self.score

            with open("highest.txt", "w") as f:
                print(self.highestscore)
                highestscore = f.write(str(self.highestscore))


        self.clear()
        self.updatescore()

    def gameover(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"SCORE = {self.score}, HIGHTEST SCORE= {self.highestscore}", True, align=ALIGNMENT, font=FONT)
        self.goto(0,0)
        self.write(f"GAME OVER",True, align=ALIGNMENT, font=FONT)