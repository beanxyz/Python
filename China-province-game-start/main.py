import turtle
import pandas

screen = turtle.Screen()
screen.title("中国省份记忆测试")

# image = "blank_states_img.gif"

image= "china.gif"
screen.addshape(image)

turtle.shape(image)

correct=[]
data = pandas.read_csv("province.csv")

allstate= data.state.to_list()

faillist=[]

while len(correct) < 28:
    answer = screen.textinput(title=f"{len(correct)}/34 正确", prompt="省份名字是什么?")
    if answer == 'Exit':
        print("exit")
        # for item in allstate:
        #     if item in correct:
        #         pass
        #     else:
        #         print(item)
        #         faillist.append(item)

        faillist = [ state for state in allstate if (state not in correct)]


        print(faillist)
        newdata= pandas.DataFrame(faillist)
        newdata.to_csv("newdata.csv")
        break

    state_data = data[data.state == answer]



    if len(state_data) == 0:
        print("No such state")
    else:
        # print(state)
        name = state_data.state.item()
        x = state_data.x
        y = state_data.y
        print(name)
        print(x)
        print(y)
        display = turtle.Turtle()
        display.hideturtle()
        display.penup()
        display.goto(int(x),int(y))
        display.write(name,align="center",font=("Arial",8,"normal"))
        correct.append(answer)


# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
#
# # screen.exitonclick()