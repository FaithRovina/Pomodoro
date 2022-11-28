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
rep = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(time_count, text="00:00")
    timer_label.config(text="Timer")
    check_mark.config(text="")
    global rep
    rep = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global rep
    rep += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # for 1/3/5/7 rep
    if rep % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif rep % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=YELLOW)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = (count % 60)

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(time_count, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = (math.floor(rep / 2))
        for _ in range(work_sessions):
            mark += "✔"
        check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=PINK)

canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
time_count = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=PINK)
timer_label.grid(column=1, row=0)

# buttons

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(fg=GREEN, bg=PINK, highlightthickness=0)
check_mark.grid(column=1, row=3)
window.mainloop()
