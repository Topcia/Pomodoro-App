import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
oke = ""

# ---------------------------- TIMER RESET ------------------------------- # 


# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    mins  = int(count/60)
    secs = count - mins*60
    if secs < 10:
        secs = f"0{secs}"
    canvas.itemconfig(timer_text, text=f"{mins}:{secs}")
    if count > 0:
        global timer
        timer = window.after(1, countdown, count - 1)
    else:
        start()
        if REPS % 9 == 0:
            pass
        elif REPS % 2 == 0:
            global oke
            oke = oke + "✔"
            checked_marks.config(text=oke, bg=YELLOW, fg="green",font=(FONT_NAME, 10, "bold"))




# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


def start():
    global REPS
    REPS += 1
    if REPS % 9 == 0:
        countdown(LONG_BREAK_MIN * 60)
        label.config(text="Break", font=(FONT_NAME, 50, "bold"), fg=GREEN)
    elif REPS % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        label.config(text="Break", font=(FONT_NAME, 50, "bold"), fg=GREEN)
    else:
        countdown(WORK_MIN * 60)
        label.config(text="Work ", font=(FONT_NAME, 50, "bold"), fg=RED)

def reset():
    window.after_cancel(timer)
    checked_marks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN)

button1 = tkinter.Button(text="Start", command=start)
button1.grid(column=0, row=2)

button1 = tkinter.Button(text="Reset", command=reset)
button1.grid(column=2, row=2)


checked_marks = tkinter.Label(text="", bg=YELLOW, fg="green")
checked_marks.config(font=(FONT_NAME, 10, "bold"))
checked_marks.grid(column=1, row=3)


label = tkinter.Label(bg=YELLOW, highlightthickness=0)
label.config(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN)
label.grid(column=1, row=0)


window.mainloop()