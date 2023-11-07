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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it's the 8th rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    # If it's 2nd/4th/6th rep:
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        # If it's the 1st/3rd/5th/7th rep:
        count_down(work_sec)  # countdown for work_sec
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    # Set the format of time i.e "01:35"
    count_minute = math.floor(count / 60)   # returns the largest integer <= x
    count_sec = count % 60  # 100/60 = 1    100-60=40 as remainder

    # Dynamic typing -> change the variable datatype by changing the content in that variable
    if count_sec < 10:  # count_sec is integer
        count_sec = f"0{count_sec}"    # count_sec is string

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_sec}")   # change the text in the canvas
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas widget -> allows layering one thing above another
# Add Image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")   # read through a file and get hold of an image
# Add image to the canvas [arguments:x-value,y-value,image]
canvas.create_image(100, 112, image=tomato_img)
# Display text in the canvas picture [arguments:x-value,y-value,text]
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# Timer label
timer_label = Label(text="Timer", font=(FONT_NAME, 60), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# Start button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Reset button
reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

# Check mark
check_mark = Label(text="✔", fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()
