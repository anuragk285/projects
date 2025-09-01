from tkinter import *
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
tick = "✔"
ticks = ""
time = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global ticks, reps, time
    window.after_cancel(time)
    canvas.itemconfig(timer_text, text="00:00")
    tick_mark.config(text="", bg=YELLOW, fg=YELLOW)
    timer.config(text="Timer")
    ticks = ""
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, tick, ticks
    reps += 1

    if (reps%2!=0 and reps%8!=1) or (reps%8==0):
        ticks += tick
        tick_mark.config(text=ticks, fg=GREEN, bg=YELLOW)

    if reps%8 == 0:
        timer.config(text="BREAK", fg=RED)
        count_down(LONG_BREAK_MIN*60)
        ticks = ""
        tick_mark.config(text="", bg=YELLOW)
    elif reps%2 == 0:
        timer.config(text="SHORT BREAK", fg=PINK)
        count_down(SHORT_BREAK_MIN*60)
    else :
        timer.config(text="WORK", fg=GREEN)
        count_down(WORK_MIN*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global time
    count_min = count//60
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        time = window.after(1000, count_down, count-1)
    else : start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(row=1, column=1)

timer = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
timer.grid(row=0,column=1)

start = Button(text="start", highlightthickness=0, bg=YELLOW)
start.config(text="start", command=start_timer)
start.grid(row=2,column=0)

reset = Button(text="reset", highlightthickness=0, bg=YELLOW)
reset.config(text="reset", command=reset_timer)
reset.grid(row=2, column=2)

tick_mark = Label()
tick_mark.config(text="", bg=YELLOW, fg=YELLOW)
tick_mark.grid(row=3,column=1)

window.mainloop()
