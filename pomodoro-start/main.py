from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_txt, text = f"00:00")
    timer_label.config(text="Timer")
    tick_label.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global  reps
    reps += 1
    work_sec = WORK_MIN *60
    short_break_sec= SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN*60

    # 25 min work
    # 5 min break
    # 25 min work
    # 5 min break
    # 25 min work
    # 5 min break
    # 25 min work
    # 20 min break

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break",fg=RED)
    elif reps % 2 ==0:
        count_down(short_break_sec)

        timer_label.config(text="Break",fg=PINK)
    else:
        count_down(work_sec)

        timer_label.config(text="Work",fg=GREEN)


        # count_down(65)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global  timer
    print(count)
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec =f"0{count_sec}"


    canvas.itemconfig(timer_txt, text = f"{count_min}:{count_sec}")
    if count >0:
        timer = window.after(1000,count_down,count -1 )

    else:
        start_timer()
        mark = ''
        for _ in range(math.floor(reps /2)):
            mark +="🗸"
        tick_label.config(text=mark,fg = GREEN, font=(FONT_NAME,20,"bold"),bg=YELLOW,highlightthickness=0)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)




canvas = Canvas(width=220,height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(103,112,image=tomato_img)
timer_txt=canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=2)


timer_label = Label(fg=GREEN,font=(FONT_NAME,40,"bold"),text="Timer",bg=YELLOW)
timer_label.grid(column=2,row=1)

start_btn = Button(text="Start",highlightthickness=0,command = start_timer)
start_btn.grid(column=1,row=3)


reset_btn = Button(text="Reset",highlightthickness=0, command = reset_timer)
reset_btn.grid(column=3,row=3)

tick_label = Label(fg = GREEN, font=(FONT_NAME,20,"bold"),bg=YELLOW,highlightthickness=0)
tick_label.grid(column=2,row=4)



window.mainloop()