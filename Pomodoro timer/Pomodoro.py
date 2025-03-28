from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= "00:00")
    label.config(text= "Timer")
    tick.config(text= "")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    if reps == 8:
        count_down(long_break_secs)
        label.config(text= "Break", fg= GREEN)
        reps = 0
    elif reps % 2 == 1:
        count_down(work_secs)
        label.config(text= "Work", fg= PINK)
    else:
        count_down(short_break_secs)
        label.config(text= "Break", fg= RED)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    global timer
    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if count >= 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        tick.config(text= mark)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady= 50, bg= YELLOW)

label = Label(text="Timer", fg= RED, bg= YELLOW, font=(FONT_NAME, 45, "normal"))
label.grid(column= 1, row= 0)

check_mark = "✔"
tick = Label(bg= YELLOW, fg= GREEN, font=(FONT_NAME, 15, "normal"))
tick.grid(column= 1, row= 3)

canvas = Canvas(width= 204, height= 224, bg= YELLOW, highlightthickness= 0)
tomato_img = PhotoImage(file= "tomato.png")
canvas.create_image(102, 112, image= tomato_img)
timer_text = canvas.create_text(102, 130, text= "00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column= 1, row= 1)

start_button = Button(text= "Start", font= (FONT_NAME, 10, "normal"), highlightthickness= 0, command= start_timer)
start_button.grid(column= 0, row= 2)

reset_button = Button(text= "Reset", font=(FONT_NAME, 10, "normal"), highlightthickness= 0, command= reset_timer)
reset_button.grid(column= 2, row= 2)

window.mainloop()