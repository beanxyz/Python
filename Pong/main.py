from turtle import Turtle, Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.bgpic("pong.png")

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)

scoreboard= Scoreboard()
ball = Ball()
print(ball.color())
print(ball.position())
screen.update()

screen.listen()
screen.onkey(r_paddle.up,'Up')
screen.onkey(r_paddle.down,'Down')
screen.onkey(l_paddle.up,'w')
screen.onkey(l_paddle.down,'s')

game_is_on = True

first = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()
    if ball.ycor() >= 250 or ball.ycor() < -250:
        print('bounce')
        ball.bounce_x()

    if ball.xcor() > 320 and ball.distance(r_paddle)<50:
        # print("hit right paddle")
        ball.bounce_y()
        ball.move_speed*0.9

    if ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        # print("hit left paddle")
        ball.bounce_y()
        ball.move_speed * 0.9

    if ball.xcor() > 380:

        ball.reset_posiiton()
        scoreboard.l_score()


    if ball.xcor() < -380:
        ball.reset_posiiton()
        scoreboard.r_score()



screen.exitonclick()

