from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#初始化画布，设置长度，宽度和标题
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

#tracer设置为0的作用是关闭动画效果，我们通过timer设置延时，然后通过update手动刷新界面，否则默认的动画效果看起来就是每个方块的移动效果
#想象一下GIF或者CRT显示器的原理，多个画面连续刷新，看起来就像动起来一样
screen.tracer(0)

#实例化三个对象
snake_segments = Snake()
food = Food()
scoreboard = Scoreboard()

#监听上下左右的键盘操作
screen.listen()
screen.onkey(snake_segments.up, "Up")
screen.onkey(snake_segments.down, "Down")
screen.onkey(snake_segments.left, "Left")
screen.onkey(snake_segments.right, "Right")

#布尔值判断是否结束游戏
game_is_on = True
while game_is_on:

#每次停顿0.1秒后刷新一下界面，然后蛇移动一下
    screen.update()
    time.sleep(0.1)
    snake_segments.move()

# 如果蛇头碰见食物了，那么食物刷新随机生成一下，分数加一，蛇身长度加一
    if snake_segments.head.distance(food) < 15:
        print("yum yum yum")
        food.refresh()
        scoreboard.addscore()
        snake_segments.add_segment()

# 如果蛇头撞墙了，那么Game over

    if snake_segments.head.xcor() > 280 or snake_segments.head.xcor() < -280 or snake_segments.head.ycor() > 280 or snake_segments.head.ycor() < -280:
        game_is_on = False
        scoreboard.gameover()

# 如果蛇头撞到身子了，那么Game over，注意列表是从第二节开始的，排除蛇头

    for seg in snake_segments.segments[1:]:

        if snake_segments.head.distance(seg) < 10:
            game_is_on = False
            scoreboard.gameover()

screen.exitonclick()
